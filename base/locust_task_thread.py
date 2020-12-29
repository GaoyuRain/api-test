"""
author :rain
Date : 2020/11/16
Description : 启动 locust进程的线程
"""
import subprocess
from threading import Thread

from base.locust_config import START_LOCUST_CMD_MASTER, START_LOCUST_CMD_WORKER


class TaskThread(Thread):
    def __init__(self, is_master, file_name):
        '''
        多进程启动locust的任务线程
        :param is_master: 是否主进程
        :param file_name: 脚本文件名
        '''
        super().__init__()
        self.is_master = is_master
        self.file_name = file_name

    def run(self):
        # print('start worker')
        if self.is_master:
            subprocess.call(START_LOCUST_CMD_MASTER % self.file_name, shell=True)
        else:
            subprocess.call(START_LOCUST_CMD_WORKER % self.file_name, shell=True)