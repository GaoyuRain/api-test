"""
author :rain
Date : 2020/07/16
Description :
# 对外 api_fj 前缀：/walkman/api_fj
# 对内 api_fj 前缀：/walkman/internal/api_fj （对内接口需走 svc
"""
import os

import yaml


def get_host(type):
    cur_host = ""
    if 'test'.__eq__(type):
        cur_host = "http://test-api.fanjiao.co/walkman/api"
        # cur_host = "http://test-api.fanjiao.co"
    elif 'pre'.__eq__(type):
        cur_host = "http://pre-api.fanjiao.co/walkman/api"
    else:
        cur_host = 'http://api.fanjiao.co/walkman/api'
    return cur_host


def get_yaml_data(file_name):
    print(file_name)
    file_path = BASE_DIR + os.sep + 'test_data' + os.sep + file_name
    # print(file_path)
    with open(file_path, 'r', encoding='UTF-8') as f:
        return yaml.safe_load(f)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# 测试的环境 pro  pre test
envir_fj = 'pro'
# 是否打印log
hasLog = True

BASE_URL = get_host(envir_fj)
# 用户信息
user_info = None
# 接口自动化用户信息存储文件名
uinfo_api_auto_file = 'uinfo_api_auto.yaml'
# 接口压测用户信息存储文件名
uinfo_api_pressure_file = 'uinfo_api_pressure.yaml'

""" 压测脚本参数数据 """
# 登录页面
login_api_data = get_yaml_data('t01_login_api_data.yaml')
# 直播页面
live_data = get_yaml_data('t02_live_api_data.yaml')
# 我的页面
my_api_data = get_yaml_data('t03_my_api_data.yaml')
# cv信息页面
cv_info_api_data = get_yaml_data('t04_cv_info_api_data.yaml')
# 剧集详情页面
album_info_api_data = get_yaml_data('t05_album_info_api_data.yaml')
# 首页页面
home_api_data = get_yaml_data('t06_home_api_data.yaml')
# 钱包页面
account_api_data = get_yaml_data('t07_account_api_data.yaml')
# 评论页面
comment_api_data = get_yaml_data('t08_comment_api_data.yaml')

if __name__ == '__main__':
    print(BASE_DIR)
    print(BASE_URL)
