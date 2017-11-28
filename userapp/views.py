# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
import os
import shutil
import uuid

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

# -------


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

