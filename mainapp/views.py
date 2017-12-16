# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import mimetypes
from collections import OrderedDict

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

    base_name = os.path.basename(path)
    bare_name = base_name.rsplit('.', 1)[0]
    md = None
    if os.path.exists(os.path.join(full_path, bare_name + '.md')):
        with open(os.path.join(full_path, bare_name + '.md')) as f:
            md = f.read().decode('utf-8').encode('utf-8')
    yaml = None
    if os.path.exists(os.path.join(full_path, bare_name + '.yaml')):
        with open(os.path.join(full_path, bare_name + '.yaml')) as f:
            yaml = f.read().decode('utf-8').encode('utf-8')
    xml = None
    if os.path.exists(os.path.join(full_path, bare_name + '.xml')):
        with open(os.path.join(full_path, bare_name + '.xml')) as f:
            xml = f.read().decode('utf-8').encode('utf-8')

    ret_map = {'code': 200, 'msg': 'Success.', 'path': path}
    if md is not None:
        ret_map['md'] = md
    if yaml is not None:
        ret_map['yaml'] = yaml
    if xml is not None:
        ret_map['xml'] = xml
    return JsonResponse(ret_map)

# -------


def _walk(cur_dir, prefix, support_format, compress_format):
    ans = dict()
    files = os.listdir(cur_dir)
    raw_names = list()
    for f in files:
        # if os.path.isfile(os.path.join(cur_dir, f)):
        #     if str(f).rsplit('.', 1)[-1] in support_format and str(f).rsplit('.', 1)[-1] != 'md':
        #         ans[f] = os.path.join(prefix, f)
        #         raw_names.append(str(f).rsplit('.', 1)[0])
        if os.path.isdir(os.path.join(cur_dir, f)):
            find_compress = None
            for c in compress_format:
                if os.path.exists(os.path.join(cur_dir, f + '.' + c)):
                    find_compress = f + '.' + c
                    break
            has_dir = False
            son_file = os.listdir(os.path.join(cur_dir, f))
            for s in son_file:
                if os.path.isdir(os.path.join(cur_dir, f, s)):
                    has_dir = True
            if has_dir:
                son = _walk(os.path.join(cur_dir, f), os.path.join(prefix, f), support_format, compress_format)
                ans[f] = {'file': False, 'name': os.path.join(prefix, f), 'sondir': son}
                if find_compress is not None:
                    ans[f]['compress'] = os.path.join(prefix, find_compress)
            else:
                ans[f] = {'file': True, 'name': os.path.join(prefix, f)}
                if find_compress is not None:
                    ans[f]['compress'] = os.path.join(prefix, find_compress)
    # for f in files:
    #     if os.path.isfile(os.path.join(cur_dir, f)):
    #         if str(f).rsplit('.', 1)[-1] == 'md' and str(f).rsplit('.', 1)[0] not in raw_names:
    #             ans[f] = os.path.join(prefix, f)
    return OrderedDict(sorted(ans.items(), key=lambda t: t[0]))
