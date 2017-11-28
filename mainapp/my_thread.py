# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import time
import shutil
import threading
from LapisServer import settings


class ScenarioThread(threading.Thread):
    def __init__(self, sess, record, script_path, worker_dir, swap_dir):
        super(ScenarioThread, self).__init__()
        self.session = sess
        self.record = record
        self.script_path = script_path
        self.worker_dir = worker_dir
        self.swap_dir = swap_dir

        self.dir_name = os.path.join(swap_dir, sess)
        self.report_path = os.path.join(self.dir_name, 'scenariores.json')
        self.stdout_path = os.path.join(self.dir_name, 'scenarioout.txt')

    def run(self):
        cout = os.popen(
            str('{} {}/scenarioTest.py --source {} --out {} 2>{}'.
                format(settings.WORKER_CMD, self.worker_dir, self.script_path, self.report_path, self.stdout_path))
        ).readlines()
        for c in cout:
            print(c)
        self.record['fin'] = 1


class SwapCleaner(threading.Thread):
    def __init__(self, sessions, status, swap_dir, timeout=3600):
        ''' default 1h timeout '''
        super(SwapCleaner, self).__init__()
        self.sessions = sessions
        self.status = status
        self.swap_dir = swap_dir
        self.timeout = timeout

    def run(self):
        while True:
            now_t = time.time()
            to_del = list()
            for sess in self.status:
                if (not self.status[sess]['lock']) and (now_t - self.status[sess]['timestamp'] > self.timeout):
                    to_del.append(sess)
            for i in to_del:
                self.sessions.remove(i)
                del self.status[i]

            print('!!!')
            if os.path.exists(self.swap_dir):
                files = os.listdir(self.swap_dir)
                for f in files:
                    print(f)
                    abs_f = os.path.join(self.swap_dir, f)
                    if os.path.exists(abs_f) and (not os.path.isfile(abs_f)):
                        if f not in self.status:
                            shutil.rmtree(abs_f)
            time.sleep(self.timeout)


