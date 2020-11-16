"""
author :rain
Date : 2020/11/13
Description : loucst 配置文件
"""
import os
import subprocess
from threading import Thread

'''locust 配置'''
# 杀掉loucst进程命令
KILL_LOSUCT_CMD = '''ps aux |grep locust  |awk '{print $2}' |xargs kill -9'''
# 有web启动locust命令  单进程
STAR_LOSCUT_WEB = 'locust -f ../case_fj/%s'
# 无web启动locust命令
STAR_LOSCUT_NO_WEB = 'locust -f ../case_fj/%s  --headless -u %d -r %d --run-time %s '
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

# 多进程启动locust
# 主进程 命令
START_LOCUST_CMD_MASTER = 'locust -f ../case_fj/%s  --master'
# 协作进程 命令
START_LOCUST_CMD_WORKER = 'locust -f ../case_fj/%s  --worker'
# 进程数
LOCUST_P = 8
