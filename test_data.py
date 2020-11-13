"""
author :rain
Date : 2020/10/29
Description : 调试用
"""
import constant
from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils


def user_login():
    r = APIUtils.send_request(constant.login_api_data.get('user_login'))
    data = dict(r.json())
    # assert 'OK' in data_fj.get('message')
    userinfo = data.get('data')
    if userinfo is not None:
        DataUtils.set_data(userinfo, 'user_info.yaml')


if __name__ == '__main__':
    pass
