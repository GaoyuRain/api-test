"""
author :rain
Date : 2020/07/16
Description :
# 对外 api_fj 前缀：/walkman/api_fj
# 对内 api_fj 前缀：/walkman/internal/api_fj （对内接口需走 svc
"""
import os

# from base_fj.fanjiao_config import get_host
# BASE_URL_INNER = BASE_URL + "/walkman/internal/api_fj"
import yaml

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_BASE_URL = "https://m.test.ximalaya.com"
UAT_BASE_URL = "https://m.uat.ximalaya.com"

# Uat
# android
HEADER6 = {'User-Agent': 'ting_6.6.93(EML-TL00,Android29)', 'Content-type': 'application/x-www-form-urlencoded',
           'Cookie': '6&_device=android&9071d20d-effe-3a28-a144-450dfdde0f77&6.6.99;6&_token=11238014&ED5FE8B0140C41A8D477DC3739FCAEC3E31860E4AD4F483610E2E70F3B1AADF5682449312EA0245M7de15d7C493900A_;'}



# test
# android cookie
HEADER1 = {'User-Agent': 'ting_6.6.93(EML-TL00,Android29)', 'Content-type': 'application/x-www-form-urlencoded',
           'Cookie': '4&_token=322709&E410EA20140CFDCF2C22B36A55C3A0C0FB4A96995895C3FF22FB7136D75B639B1A4AD2412B99191M9933558CC8A36B7_;4&_device=android&9071d20d-effe-3a28-a144-450dfdde0f77&6.6.93'}


def get_host(type):
    if 'test'.__eq__(type):
        cur_host = "http://test-api.fanjiao.co/walkman/api"
    elif 'pre'.__eq__(type):
        cur_host = "http://pre-api.fanjiao.co/walkman/api"
    else:
        cur_host = 'http://api.fanjiao.co/walkman/api'
    return cur_host


def get_yaml_data(file_name):
    print(file_name)
    file_path = BASE_DIR + os.sep + 'data_fj' + os.sep + file_name
    # print(file_path)
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


# 测试环境 pro  pre test
envir = 'pro'

BASE_URL = get_host(envir)
# 用户信息
user_info = None
# 用户信息存放文件名
user_info_file = 'user_info_test.yaml' if 'test'.__eq__(envir) else 'user_info_pro.yaml'
# 是否打印log
hasLog = True

""" 参数数据 """
# 登录页面
login_api_data = get_yaml_data('t01_login_api_data.yaml')
# 直播页面
# live_data = None
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

# constant.login_api_data = DataUtils.get_yaml_data('t01_login_api_data.yaml')
# constant.my_api_data = DataUtils.get_yaml_data('t03_my_api_data.yaml')
# constant.cv_info_api_data = DataUtils.get_yaml_data('t04_cv_info_api_data.yaml')
# constant.album_info_api_data = DataUtils.get_yaml_data('t05_album_info_api_data.yaml')
# constant.home_api_data = DataUtils.get_yaml_data('t06_home_api_data.yaml')
# constant.account_api_data = DataUtils.get_yaml_data('t07_account_api_data.yaml')
# constant.comment_api_data = DataUtils.get_yaml_data('t08_comment_api_data.yaml')

if __name__ == '__main__':
    pass
