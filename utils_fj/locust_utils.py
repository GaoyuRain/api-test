"""
author :rain
Date : 2020/11/16
Description :
"""
import subprocess
from threading import Thread

from base_fj.locust_config import STAR_LOSCUT_WEB, STAR_LOSCUT_NO_WEB, STOP_CMD, LOCUST_U, LOCUST_R, RUN_TIME, LOCUST_P, \
    START_LOCUST_CMD_MASTER, START_LOCUST_CMD_WORKER, IS_MASTER_MODE, HAS_WEB, IS_STOP_DONE
from base_fj.locust_task_thread import TaskThread


class LocustUtils:
    @staticmethod
    def start_locust(file_name):
        '''
        启动locust脚本
        :param file_name: 脚本文件名
        '''
        if IS_MASTER_MODE:
            LocustUtils.__start_worker_thread(file_name)
            return
        if HAS_WEB:
            l_cmd = STAR_LOSCUT_WEB % (file_name)
        else:
            l_cmd = STAR_LOSCUT_NO_WEB % (file_name, LOCUST_U, LOCUST_R, RUN_TIME)
        if IS_STOP_DONE:
            l_cmd += STOP_CMD
        # 执行命令
        subprocess.call(l_cmd, shell=True)

    @staticmethod
    def __start_worker_thread(file_name):
        threads = []
        for i in range(LOCUST_P + 1):
            if i == 0:
                t = TaskThread(True, file_name)
            else:
                t = TaskThread(False, file_name)
            threads.append(t)
            t.start()
        for i in threads:
            i.join()


if __name__ == '__main__':
    # 例:
    print(STAR_LOSCUT_NO_WEB % ('locust_file.py', LOCUST_U, LOCUST_R, RUN_TIME) + STOP_CMD)
    print(STAR_LOSCUT_WEB)
    LocustUtils.start_locust('test_08_comment.py', is_master_mode=True)
