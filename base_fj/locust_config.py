"""
author :rain
Date : 2020/11/13
Description : loucst 配置文件
"""
import os

'''配置'''
# 杀掉loucst进程命令
KILL_LOSUCT_CMD = '''ps aux |grep locust  |awk '{print $2}' |xargs kill -9'''
# 有web启动locust命令
STAR_LOSCUT_WEB = 'locust -f %s'
# 无web启动locust命令
STAR_LOSCUT_NO_WEB = 'locust -f %s  --headless -u %d -r %d --run-time %s '
# 启动总用户数
LOCUST_U = 20
# 每秒启动几个用户
LOCUST_R = 2
# 执行时间 单位： h m s
RUN_TIME = '30s'
# 是否到时后执行完成在停止允许
IS_STOP_DONE = True
# 到时后执行完成后在停止命令
STOP_CMD = '--stop-timeout 20'


class LocustConfig:

    @staticmethod
    def locust_cmd(file_name, has_web=False, is_stop_done=True):
        '''
        获取locust启动命令
        :param file_name: 脚本文件名
        :param has_web: 是否需要web界面
        :param is_stop_done: 是否到时后执行完成在停止运行
        :return: 启动命令
        '''
        if has_web:
            return STAR_LOSCUT_WEB % (file_name)
        l_cmd = STAR_LOSCUT_NO_WEB % (file_name, LOCUST_U, LOCUST_R, RUN_TIME)
        return l_cmd + STOP_CMD if is_stop_done else l_cmd


if __name__ == '__main__':
    # 例:
    print(STAR_LOSCUT_NO_WEB % ('locust_file.py', LOCUST_U, LOCUST_R, RUN_TIME) + STOP_CMD)
    print(STAR_LOSCUT_WEB)
