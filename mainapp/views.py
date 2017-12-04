# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import mimetypes

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from LapisServer import settings


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def examples(request):
    return render(request, 'examples.html')


def tutorial(request):
    return render(request, 'tutorial.html')


def index_fileupload(request):
    f = request.FILES.get('script', None)
    if f is None:
        return JsonResponse({'code': 201, 'msg': 'No file found.'})
    name = f.name.rsplit('.', 1)[0]
    if f.size > 1048576:
        # >1M -> too large
        return JsonResponse({'code': 202, 'msg': 'File size is too large.'})
    s = f.read().decode('utf-8').encode('utf-8')
    return JsonResponse({'code': 200, 'msg': 'Success.', 'script': s, 'name': name})


def get_cloud_api_examples(request):
    support_format = ['yaml', 'xml', 'md']
    compress_format = ['zip', 'gz']

    cur_dir = os.path.join(settings.STATIC_ROOT, settings.CLOUD_API_DIR)
    res = _walk(cur_dir, '', support_format, compress_format)
    res = {'sondir': res}
    return JsonResponse({'code': 200, 'result': res})


def download_cloud_api_examples(request):
    path = request.GET.get('path', None)
    if path is None:
        return JsonResponse({'code': 201, 'msg': 'path required.'})
    full_path = os.path.join(settings.STATIC_ROOT, settings.CLOUD_API_DIR, path)
    if not os.path.exists(full_path):
        return JsonResponse({'code': 202, 'msg': 'Illegal path. File doesn\'t exists.'})
    with open(full_path, str('r')) as f:
        data = f.read()
    response = HttpResponse(data, content_type=mimetypes.guess_type(full_path)[0])
    response['Content-Disposition'] = "attachment; filename={0}".format(os.path.basename(full_path))
    response['Content-Length'] = os.path.getsize(full_path)
    return response


def read_cloud_api_examples(request):
    path = request.GET.get('path', None)
    if path is None:
        return JsonResponse({'code': 201, 'msg': 'path required.'})
    full_path = os.path.join(settings.STATIC_ROOT, settings.CLOUD_API_DIR, path)
    if not os.path.exists(full_path):
        return JsonResponse({'code': 202, 'msg': 'Illegal path. File doesn\'t exists.'})
    with open(full_path, str('r')) as f:
        s = f.read().decode('utf-8').encode('utf-8')
    supplement = ''
    if path.rsplit('.')[-1] != 'md' and os.path.exists(full_path.rsplit('.', 1)[0] + '.md'):
        with open(full_path.rsplit('.', 1)[0] + '.md', str('r')) as f:
            supplement = f.read().decode('utf-8').encode('utf-8')
    return JsonResponse({'code': 200, 'msg': 'Success.', 'script': s,
                         'supplement': supplement, 'path': path, 'format': path.rsplit('.')[-1]})

# -------


def _walk(cur_dir, prefix, support_format, compress_format):
    ans = dict()
    files = os.listdir(cur_dir)
    raw_names = list()
    for f in files:
        if os.path.isfile(os.path.join(cur_dir, f)):
            if str(f).rsplit('.', 1)[-1] in support_format and str(f).rsplit('.', 1)[-1] != 'md':
                ans[f] = os.path.join(prefix, f)
                raw_names.append(str(f).rsplit('.', 1)[0])
        elif os.path.isdir(os.path.join(cur_dir, f)):
            find_compress = None
            for c in compress_format:
                if os.path.exists(os.path.join(cur_dir, f + '.' + c)):
                    find_compress = f + '.' + c
                    break
            son = _walk(os.path.join(cur_dir, f), os.path.join(prefix, f), support_format, compress_format)
            if len(son) > 0:
                ans[f] = {'sondir': son}
                if find_compress is not None:
                    ans[f]['compress'] = os.path.join(prefix, find_compress)
    for f in files:
        if os.path.isfile(os.path.join(cur_dir, f)):
            if str(f).rsplit('.', 1)[-1] == 'md' and str(f).rsplit('.', 1)[0] not in raw_names:
                ans[f] = os.path.join(prefix, f)
    return ans
