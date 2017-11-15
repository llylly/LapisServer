# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import json
import uuid
import time
from parse import parse
from LapisServer import settings
from django.http import JsonResponse
import mainapp.my_thread

worker_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'worker')
swap_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'swap')

sessions = list()
status = dict()

cleaner = None


def session_verify(request):
    global cleaner
    input_session = request.GET.get('id', None)
    if input_session is None:
        return JsonResponse({'code': 201, 'msg': 'No \'id\' specified.'})
    else:
        input_session = str(input_session)
        out_session = None
        if input_session in sessions:
            out_session = input_session
        else:
            while out_session is None or out_session in sessions:
                out_session = uuid.uuid1().get_hex()
            sessions.append(out_session)
            status[out_session] = dict()
            status[out_session]['status'] = 0
            status[out_session]['lock'] = False
        status[out_session]['timestamp'] = time.time()
        """Open the cleaner"""
        if cleaner is None:
            # default session long: 1h
            cleaner = mainapp.my_thread.SwapCleaner(sessions, status, swap_dir)
            cleaner.start()
        return JsonResponse({'code': 200, 'id': out_session})


def script_parse(request):
    session = request.POST.get('session', None)
    type = request.POST.get('type', None)
    text = request.POST.get('text', None)
    if (session is None) or (str(session) not in sessions):
        return JsonResponse({'code': 201, 'msg': 'Illegal session.'})
    session = str(session)
    if type is None or (str(type) != 'YAML' and str(type) != 'XML'):
        return JsonResponse({'code': 202, 'msg': 'Illegal script format.'})
    if text is None:
        return JsonResponse({'code': 203, 'msg': 'No \'text\' sepcified.'})

    suffix = ''
    if str(type) == 'YAML':
        suffix = '.yaml'
    if str(type) == 'XML':
        suffix = '.xml'

    dir_name = os.path.join(swap_dir, session)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    script_path = os.path.join(dir_name, 'script{}'.format(suffix))
    parseres_path = os.path.join(dir_name, 'parse_res.json')
    with open(script_path, str('w')) as f:
        f.write(text.encode('utf-8'))
    os.popen(
        str('{} {}/parser.py --source {} --out {}'.format(settings.WORKER_CMD, worker_dir, script_path, parseres_path)))
    with open(parseres_path, str('r')) as f:
        result = json.load(f)
    if result['docParse'] and result['apiParse']:
        status[session]['status'] = 1
        status[session]['scriptPath'] = 'script{}'.format(suffix)
        status[session]['apiList'] = result['apiNames']
        if result['scenarioParse'] and result['configParse']:
            status[session]['status'] = 2

    return JsonResponse({'code': 200, 'msg': 'success', 'result': result})


def apidata_gen(request):
    session = request.POST.get('session', None)
    method = request.POST.get('method', None)
    api = request.POST.get('api', None)
    if (session is None) or (str(session) not in sessions):
        return JsonResponse({'code': 201, 'msg': 'Illegal session.'})
    session = str(session)
    if method is None or (str(method) != 'get' and str(method) != 'post'):
        return JsonResponse({'code': 202, 'msg': 'Invalid \'method\'.'})
    if status[session]['status'] < 1:
        return JsonResponse({'code': 203, 'msg': 'Not parsed.'})
    if api is None:
        return JsonResponse({'code': 204, 'msg': '\'api\' required'})
    apiList = status[session]['apiList']
    find = False
    for item in apiList:
        if str(api) == item['name'] and str(method) == item['method']:
            find = True
    if not find:
        return JsonResponse({'code': 205, 'msg': 'Specified API not found.'})

    status[session]['lock'] = True
    dir_name = os.path.join(swap_dir, session)
    script_path = os.path.join(dir_name, status[session]['scriptPath'])
    genres_path = os.path.join(dir_name, 'gen_res.json')
    cout = os.popen(
        str('{} {}/datagen.py --source {} --name {} --method {} --out {}'.
            format(settings.WORKER_CMD, worker_dir, script_path, api, method, genres_path))
    ).readlines()
    status[session]['lock'] = False
    for c in cout:
        print(c)
    with open(genres_path, str('r')) as f:
        result = json.load(f)
    status[session]['lock'] = False
    return JsonResponse({'code': 200, 'msg': 'success', 'result': result})


def single_test(request):
    session = request.POST.get('session', None)
    if (session is None) or (str(session) not in sessions):
        return JsonResponse({'code': 201, 'msg': 'Illegal session.'})
    session = str(session)
    if status[session]['status'] < 1:
        return JsonResponse({'code': 203, 'msg': 'Not parsed.'})

    method = request.POST.get('method', None)
    if method is None or (str(method) != 'get' and str(method) != 'post'):
        return JsonResponse({'code': 202, 'msg': 'Invalid \'method\'.'})
    method = str(method)

    api = request.POST.get('api', None)
    if api is None:
        return JsonResponse({'code': 204, 'msg': '\'api\' required'})
    api = str(api)

    apiList = status[session]['apiList']
    find = False
    for item in apiList:
        if api == item['name'] and method == item['method']:
            find = True
    if not find:
        return JsonResponse({'code': 205, 'msg': 'Specified API not found.'})

    isali = request.POST.get('isali', None)
    try:
        isali = str(isali)
        assert isali == 'true' or isali == 'false'
        if isali == 'true':
            isali = True
        else:
            isali = False
    except:
        return JsonResponse({'code': 206, 'msg': '\'isali\' parameter format wrong.'})

    secret_key = 'invalid'
    if isali:
        try:
            secret_key = request.POST.get('secret_key', None)
            secret_key = str(secret_key)
        except:
            return JsonResponse({'code': 207, 'msg': '\'secret_key\' required.'})

    timeout = request.POST.get('timeout', None)
    try:
        timeout = int(timeout)
        assert timeout > 0
    except:
        return JsonResponse({'code': 208, 'msg': '\'timeout\' should be a positive integer.'})

    status[session]['lock'] = True
    dir_name = os.path.join(swap_dir, session)
    script_path = os.path.join(dir_name, status[session]['scriptPath'])
    singleres_path = os.path.join(dir_name, 'singleres.json')

    cout = os.popen(
        str('{} {}/singleAPITest.py --source {} --name {} --method {} --isali {} --secret_key {} --timeout {} --out {}'.
            format(settings.WORKER_CMD, worker_dir, script_path, api, method,
                   isali, secret_key, timeout, singleres_path))
    ).readlines()
    for c in cout:
        print(c)
    with open(singleres_path, str('r')) as f:
        result = json.load(f)
    status[session]['lock'] = False
    return JsonResponse({'code': 200, 'msg': 'success', 'result': result})


def scenario_test(request):
    session = request.POST.get('session', None)
    if (session is None) or (str(session) not in sessions):
        return JsonResponse({'code': 201, 'msg': 'Illegal session.'})
    session = str(session)
    if status[session]['status'] < 2:
        return JsonResponse({'code': 203, 'msg': 'Not parsed or scenario config invalid.'})

    status[session]['lock'] = True
    status[session]['scenarioStat'] = {'fin': 0, 'caseN': 0, 'stepN': 0}
    dir_name = os.path.join(swap_dir, session)
    script_path = os.path.join(dir_name, status[session]['scriptPath'])
    executor = mainapp.my_thread.ScenarioThread(session, status[session]['scenarioStat'], script_path,
                                                worker_dir, swap_dir)
    status[session]['scenarioStat']['executor'] = executor
    executor.start()
    return JsonResponse({'code': 200, 'msg': 'running'})


def scenario_test_query(request):

    def refresh_case_n(session, stat):
        out_path = stat['executor'].stdout_path
        if os.path.exists(out_path):
            with open(out_path, str('r')) as nowf:
                for line in nowf.readlines():
                    if line.count('Case #') > 0:
                        try:
                            res = parse('Case #{:d}', line)
                            stat['caseN'] = res.fixed[0] + 1
                        except Exception:
                            pass
                    if line.count('step #') > 0:
                        try:
                            res = parse('{}step #{:d}{}', line)
                            stat['stepN'] = res.fixed[1]
                        except Exception:
                            pass

    session = request.POST.get('session', None)
    if (session is None) or (str(session) not in sessions):
        return JsonResponse({'code': 201, 'msg': 'Illegal session.'})
    session = str(session)
    status[session]['timestamp'] = time.time()
    if status[session]['status'] < 2:
        return JsonResponse({'code': 203, 'msg': 'Not parsed or scenario config invalid.'})

    if 'scenarioStat' not in status[session]:
        status[session]['lock'] = False
        return JsonResponse({'code': 200, 'stat': -1, 'msg': 'Not start.'})
    stat = status[session]['scenarioStat']
    refresh_case_n(session, stat)
    if stat['fin'] == 0:
        return JsonResponse({'code': 200, 'stat': 0, 'caseN': stat['caseN'], 'stepN': stat['stepN'], 'msg': 'Running'})
    if stat['fin'] == 1:
        with open(str(stat['executor'].report_path), str('r')) as f:
            result = json.load(f)
        status[session]['lock'] = False
        return JsonResponse({'code': 200, 'stat': 1, 'caseN': stat['caseN'], 'stepN': stat['stepN'], 'result': result,
                             'msg': 'finished'})

