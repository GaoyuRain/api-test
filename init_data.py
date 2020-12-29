"""
author :rain
Date : 2020/11/03
Description : 初始化测试数据
"""

import requests

import constant
from base.fanjiao_config import FanjiaoConfig
from constant import BASE_URL
from test_utils.data_utils import DataUtils
from test_utils.log_utils import LogUtils


def user_login(phone):
    verift_url = BASE_URL + '/user/verify_code'
    params1 = {'zone': '+99', 'phone': '19999999' + str(phone)}
    r1 = requests.get(verift_url, params=params1, headers=FanjiaoConfig.signature_fj(params1))
    LogUtils.print_response(r1)

    login_url = BASE_URL + '/user/login'
    params2 = {'zone': '+99', 'phone': '19999999' + str(phone), 'verify_code': '0000', 'device_type': 2}
    r2 = requests.post(login_url, json=params2, headers=FanjiaoConfig.signature_fj(params2, 'post'))
    LogUtils.print_response(r2)
    data = dict(r2.json()).get('data')

    return data


def crest_data():
    uinfo_list = []
    for i in range(910, 920):
        data = user_login(i)
        login_token = data.get('token')
        uid = data.get('user').get('uid')
        nickname = data.get('user').get('nickname')
        avatar = data.get('user').get('avatar')
        uinfo = {'token': login_token, 'uid': uid, 'nickname': nickname, 'avatar': avatar}
        uinfo_list.append(uinfo)
    DataUtils.set_data(uinfo_list, constant.uinfo_api_pressure_file)
    print(uinfo_list)


if __name__ == '__main__':
    crest_data()
