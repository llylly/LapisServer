# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
import os
import shutil
import uuid
import mimetypes

user_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'users')

username_id_map = dict()
username_passwd_map = dict()


def register(request):
    _refresh()
    username = request.POST.get('username', None)
    passwd = request.POST.get('passwd', None)

    if username is None:
        return JsonResponse({'code': '201', 'msg': 'Username required.'})
    if passwd is None:
        return JsonResponse({'code': '202', 'msg': 'Password required.'})
    username = str(username)
    passwd = str(passwd)
    if len(username) == 0:
        return JsonResponse({'code': '203', 'msg': 'Illegal username.'})
    if len(passwd) == 0:
        return JsonResponse({'code': '204', 'msg': 'Illegal password.'})
    if username in username_id_map:
        return JsonResponse({'code': '205', 'msg': 'Username exists.'})

    id = None
    while id is None or id in username_id_map:
        id = uuid.uuid4().get_hex()[0:15]
    username_id_map[username] = id
    username_passwd_map[username] = passwd
    if os.path.exists(os.path.join(user_dir, id)):
        shutil.rmtree(os.path.join(user_dir, id))
    os.makedirs(os.path.join(user_dir, id))
    with open(os.path.join(user_dir, id, 'meta.txt'), str('w')) as f:
        f.write(str('{}\n').format(username))
        f.write(str('{}\n').format(passwd))

    request.session['user_id'] = id
    request.session.set_expiry(0)

    return JsonResponse({'code': '200', 'msg': 'Success.'})


def login(request):
    _refresh()
    username = request.POST.get('username', None)
    passwd = request.POST.get('passwd', None)

    if username is None:
        return JsonResponse({'code': '201', 'msg': 'Username required.'})
    if passwd is None:
        return JsonResponse({'code': '202', 'msg': 'Password required.'})
    username = str(username)
    passwd = str(passwd)
    if username in username_id_map and username_passwd_map[username] == passwd:
        request.session['user_id'] = username_id_map[username]
        request.session.set_expiry(0)
        return JsonResponse({'code': '200', 'msg': 'success.'})
    elif username in username_id_map:
        return JsonResponse({'code': '206', 'msg': 'Wrong password.'})
    else:
        return JsonResponse({'code': '207', 'msg': 'Username does not exist.'})


def get_status(request):
    _refresh()
    userid = request.session.get('user_id', None)
    if userid is None:
        return JsonResponse({'code': '208', 'msg': 'Not login.'})
    else:
        try:
            with open(os.path.join(user_dir, userid, 'meta.txt'), str('r')) as f:
                lines = f.readlines()
                username = lines[0][:-1]
        except Exception as e:
            print(e.message)
            return JsonResponse({'code': '209', 'msg': 'Inner record discrepancy.'})
        return JsonResponse({'code': '200', 'msg': 'Login.', 'username': username})


def logout(request):
    _refresh()
    userid = request.session.get('user_id', None)
    if userid is not None:
        del request.session['user_id']
    return JsonResponse({'code': '200', 'msg': 'Success.'})


def change_passwd(request):
    _refresh()
    oldpass = request.POST.get('old_passwd', None)
    newpass = request.POST.get('new_passwd', None)

    if oldpass is None:
        return JsonResponse({'code': '210', 'msg': 'Old Password Required.'})
    if newpass is None:
        return JsonResponse({'code': '211', 'msg': 'New Password Required.'})
    oldpass = str(oldpass)
    newpass = str(newpass)
    if len(oldpass) == 0:
        return JsonResponse({'code': '212', 'msg': 'Illegal old password.'})
    if len(newpass) == 0:
        return JsonResponse({'code': '213', 'msg': 'Illegal new password.'})
    userid = request.session.get('user_id', None)
    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    try:
        with open(os.path.join(user_dir, userid, 'meta.txt'), str('r')) as f:
            lines = f.readlines()
            username = lines[0][:-1]
            real_oldpass = lines[1][:-1]
    except Exception:
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})
    if real_oldpass != oldpass:
        return JsonResponse({'code': '216', 'msg': 'Wrong old password.'})

    with open(os.path.join(user_dir, userid, 'meta.txt'), str('w')) as f:
        f.write(str('{}\n').format(username))
        f.write(str('{}\n').format(newpass))
    username_passwd_map[username] = newpass
    return JsonResponse({'code': '200', 'msg': 'Success.'})

# ------


def get_filelist(request):
    _refresh()
    userid = request.session.get('user_id', None)
    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    if not os.path.exists(os.path.join(user_dir, userid, 'meta.txt')):
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})

    files = os.listdir(os.path.join(user_dir, userid))
    legal_files = list()
    for f in files:
        if os.path.exists(os.path.join(user_dir, userid, f, 'meta.txt')):
            legal_files.append(f)
    return JsonResponse({'code': '200', 'result': legal_files})


def load_file(request):
    _refresh()
    userid = request.session.get('user_id', None)
    filename = request.POST.get('filename', None)
    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    if not os.path.exists(os.path.join(user_dir, userid, 'meta.txt')):
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})
    if filename is None:
        return JsonResponse({'code': '216', 'msg': 'Filename required.'})
    filename = str(filename)

    try:
        with open(os.path.join(user_dir, userid, filename, 'meta.txt'), str('r')) as f:
            ver_cnt = int(f.readline())
        assert ver_cnt > 0
        assert os.path.exists(os.path.join(user_dir, userid, filename, str('{}.txt').format(ver_cnt - 1)))
    except Exception as e:
        print(e.message)
        return JsonResponse({'code': '217', 'msg': 'Illegal filename.'})

    with open(os.path.join(user_dir, userid, filename, str('{}.txt').format(ver_cnt - 1)), str('r')) as f:
        s = f.read().decode('utf-8').encode('utf-8')
    return JsonResponse({'code': '200', 'msg': 'Success.', 'script': s})


def save_file(request):
    _refresh()
    userid = request.session.get('user_id', None)
    filename = request.POST.get('filename', None)
    script = request.POST.get('script', None)
    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    if not os.path.exists(os.path.join(user_dir, userid, 'meta.txt')):
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})
    if filename is None:
        return JsonResponse({'code': '216', 'msg': 'Filename required.'})
    filename = str(filename)
    if script is None:
        return JsonResponse({'code': '218', 'msg': 'Script is required.'})
    if filename.startswith('.'):
        return JsonResponse({'code': '221', 'msg': 'Illegal filename.'})

    _save_file(user_dir, userid, filename, script)

    return JsonResponse({'code': '200', 'msg': 'Success.'})


def rename_file(request):
    _refresh()
    userid = request.session.get('user_id', None)
    oldname = request.POST.get('oldname', None)
    newname = request.POST.get('newname', None)

    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    if not os.path.exists(os.path.join(user_dir, userid, 'meta.txt')):
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})
    if oldname is None or newname is None:
        return JsonResponse({'code': '216', 'msg': 'Old name and new name are required.'})
    oldname = str(oldname)
    newname = str(newname)

    if not os.path.exists(os.path.join(user_dir, userid, oldname, 'meta.txt')):
        return JsonResponse({'code': '219', 'msg': 'Filename does not exist.'})
    if os.path.exists(os.path.join(user_dir, userid, newname)):
        return JsonResponse({'code': '220', 'msg': 'New filename is illegal. Maybe it has been used.'})
    os.rename(os.path.join(user_dir, userid, oldname), os.path.join(user_dir, userid, newname))

    return JsonResponse({'code': '200', 'msg': 'Success.'})


def del_file(request):
    _refresh()
    userid = request.session.get('user_id', None)
    filename = request.POST.get('filename', None)

    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    if not os.path.exists(os.path.join(user_dir, userid, 'meta.txt')):
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})
    if filename is None:
        return JsonResponse({'code': '216', 'msg': 'Filename required.'})
    filename = str(filename)

    if not os.path.exists(os.path.join(user_dir, userid, filename, 'meta.txt')):
        return JsonResponse({'code': '219', 'msg': 'Filename does not exist.'})
    shutil.rmtree(os.path.join(user_dir, userid, filename))

    return JsonResponse({'code': '200', 'msg': 'Success.'})


def file_import(request):
    _refresh()
    userid = request.session.get('user_id', None)
    num = request.POST.get('num', None)

    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    if not os.path.exists(os.path.join(user_dir, userid, 'meta.txt')):
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})
    try:
        num = int(num)
    except Exception:
        return JsonResponse({'code': '221', 'msg': 'Illegal "num" parameter.'})

    if os.path.exists(os.path.join(user_dir, userid, '.__tmp__')):
        shutil.rmtree(os.path.join(user_dir, userid, '.__tmp__'))
    tmp_dir = os.path.join(user_dir, userid, '.__tmp__')
    origin_dir = os.path.join(user_dir, userid, '.__tmp__/original')
    decompressed_dir = os.path.join(user_dir, userid, '.__tmp__/decompressed')
    os.makedirs(origin_dir)
    os.makedirs(decompressed_dir)

    size_limit = 10485760
    now_size = 0

    for i in range(num):
        nowf = request.FILES.get('file{}'.format(i), None)
        if nowf is None:
            shutil.rmtree(tmp_dir)
            return JsonResponse({'code': '222', 'msg': '"file{}" parameter is illegal.'.format(i)})
        now_size += nowf.size
        if now_size > size_limit:
            shutil.rmtree(tmp_dir)
            return JsonResponse({'code': '223', 'msg': 'Exceed size limit.'})
        with open(os.path.join(origin_dir, nowf.name), str('w')) as f:
            f.write(nowf.read())
        if nowf.name.endswith('.zip'):
            print(os.popen('unzip -qq -n {} -d {}'.format(os.path.join(origin_dir, nowf.name), origin_dir)).readlines())

    _traverse_move(origin_dir, decompressed_dir, ['.yaml', '.xml'])
    dec_files = os.listdir(decompressed_dir)
    for fname in dec_files:
        if fname.endswith('.yaml') or fname.endswith('.xml'):
            with open(os.path.join(decompressed_dir, fname)) as f:
                script = f.read().decode('utf-8')
            _save_file(user_dir, userid, fname.rsplit('.', 2)[0], script)
    shutil.rmtree(tmp_dir)

    return JsonResponse({'code': '200', 'msg': 'Success.'})


def clean_all(request):
    _refresh()
    userid = request.session.get('user_id', None)

    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    if not os.path.exists(os.path.join(user_dir, userid, 'meta.txt')):
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})

    files = os.listdir(os.path.join(user_dir, userid))
    for f in files:
        if os.path.exists(os.path.join(user_dir, userid, f, 'meta.txt')):
            shutil.rmtree(os.path.join(user_dir, userid, f))
    return JsonResponse({'code': '200', 'msg': 'Success.'})


def make_download_all(request):
    _refresh()
    userid = request.session.get('user_id', None)

    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    if not os.path.exists(os.path.join(user_dir, userid, 'meta.txt')):
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})

    if os.path.exists(os.path.join(user_dir, userid, '.__tmp2__')):
        shutil.rmtree(os.path.join(user_dir, userid, '.__tmp2__'))
    tmp_dir = os.path.join(user_dir, userid, '.__tmp2__')
    os.makedirs(tmp_dir)
    if os.path.exists(os.path.join(user_dir, userid, '.__tmp3__')):
        shutil.rmtree(os.path.join(user_dir, userid, '.__tmp3__'))
    os.makedirs(os.path.join(user_dir, userid, '.__tmp3__'))

    files = os.listdir(os.path.join(user_dir, userid))
    for f in files:
        if os.path.exists(os.path.join(user_dir, userid, f, 'meta.txt')):
            with open(os.path.join(user_dir, userid, f, 'meta.txt')) as nf:
                num = int(nf.readline()) - 1
            shutil.copy(os.path.join(user_dir, userid, f, '{}.txt'.format(num)),
                        os.path.join(tmp_dir, '{}.txt'.format(f)))
            format = '.yaml'
            with open(os.path.join(tmp_dir, '{}.txt'.format(f))) as nf:
                str = nf.read().decode('utf-8')
                if str.find('<?xml') == 0:
                    format = '.xml'
            os.rename(os.path.join(tmp_dir, '{}.txt'.format(f)), os.path.join(tmp_dir, '{}{}'.format(f, format)))
    print(os.popen('cd {} && zip -q -r ../.__tmp3__/documents.zip *'.format(tmp_dir)).readlines())

    shutil.rmtree(tmp_dir)

    return JsonResponse({'code': '200', 'msg': 'Success.'})


def download_all(request):
    _refresh()
    userid = request.session.get('user_id', None)

    if userid is None:
        return JsonResponse({'code': '214', 'msg': 'Not login.'})
    if not os.path.exists(os.path.join(user_dir, userid, 'meta.txt')):
        return JsonResponse({'code': '215', 'msg': 'Inner record discrepancy.'})

    full_path = os.path.join(user_dir, userid, '.__tmp3__', 'documents.zip')
    if os.path.exists(full_path):
        with open(full_path) as f:
            data = f.read()
        response = HttpResponse(data, content_type=mimetypes.guess_type(full_path)[0])
        response['Content-Disposition'] = "attachment; filename={0}".format(os.path.basename(full_path))
        response['Content-Length'] = os.path.getsize(full_path)
        return response
    else:
        return JsonResponse({'code': '221', 'msg': 'File not found.'})


# -------


def _save_file(user_dir, userid, filename, script):
    if not os.path.exists(os.path.join(user_dir, userid, filename, 'meta.txt')):
        if os.path.exists(os.path.join(user_dir, userid, filename)):
            shutil.rmtree(os.path.join(user_dir, userid, filename))
        os.makedirs(os.path.join(user_dir, userid, filename))
        with open(os.path.join(user_dir, userid, filename, 'meta.txt'), str('w')) as f:
            f.write(str('0'))

    with open(os.path.join(user_dir, userid, filename, 'meta.txt'), str('r')) as f:
        ver_cnt = int(f.readline())
    with open(os.path.join(user_dir, userid, filename, str('{}.txt').format(ver_cnt)), str('w')) as f:
        f.write(script.encode('utf-8'))
    with open(os.path.join(user_dir, userid, filename, 'meta.txt'), str('w')) as f:
        f.write(str('{}').format(ver_cnt + 1))


def _traverse_move(source, output, format_list):
    fs = os.listdir(source)
    for nowf in fs:
        if os.path.isdir(os.path.join(source, nowf)):
            _traverse_move(os.path.join(source, nowf), output, format_list)
        if os.path.isfile(os.path.join(source, nowf)):
            legal = False
            for format in format_list:
                if str(nowf).endswith(format):
                    legal = True
            if legal:
                shutil.copy(os.path.join(source, nowf), os.path.join(output, nowf))


def _refresh():
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    username_id_map.clear()
    username_passwd_map.clear()
    ids = os.listdir(user_dir)
    for id in ids:
        if os.path.exists(os.path.join(user_dir, id, 'meta.txt')):
            try:
                with open(os.path.join(user_dir, id, 'meta.txt'), str('r')) as f:
                    lines = f.readlines()
                    now_user = lines[0][:-1]
                    now_passwd = lines[1][:-1]
            except Exception:
                continue
            username_id_map[now_user] = id
            username_passwd_map[now_user] = now_passwd

