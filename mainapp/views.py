# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def examples(request):
    return render(request, 'examples.html')


def index_fileupload(request):
    f = request.FILES.get('script', None)
    if f is None:
        return JsonResponse({'code': 201, 'msg': 'No file found.'})
    if f.size > 1048576:
        # >1M -> too large
        return JsonResponse({'code': 202, 'msg': 'File size is too large.'})
    s = f.read().decode('utf-8').encode('utf-8')
    return JsonResponse({'code': 200, 'msg': 'Success.', 'script': s})
