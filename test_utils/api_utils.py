"""
author :rain
Date : 2020/10/27
Description :
"""
import requests

import constant
from base.fanjiao_config import FanjiaoConfig
from test_utils.data_utils import DataUtils
from test_utils.log_utils import LogUtils


class APIUtils:

    @staticmethod
    def send_auto_request(params_data):
        '''
        发送请求的方法
        接口自动化脚本调用
        :param params_data: 接口的参数url等信息
        :return: 响应response
        '''
        url = constant.BASE_URL + params_data.get('url')
        params = params_data.get('params')
        type = params_data.get('type').lower()
        header = DataUtils.get_user_info_auto()
        header.update(FanjiaoConfig.signature_fj(params, type))

        requests.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        if 'get'.__eq__(type):
            r = requests.get(url, headers=header, params=params, timeout=10)
        else:
            r = requests.post(url, headers=header, json=params, timeout=10)
        LogUtils.print_response(r, params_data.get('comment'), isformart=True)
        return r

    @staticmethod
    def send_pre_req(req, url_data):
        '''
        发送请求的方法
        压测脚本调用
        :param req: 请求client
        :param url_data: 接口的参数url等信息
        :return: 响应response
        '''
        # 压测接口调用
        api = url_data.get('url')
        url = constant.BASE_URL + api
        params = url_data.get('params')
        type = url_data.get('type').lower()
        header = DataUtils.get_user_info_pressure()
        header.update(FanjiaoConfig.signature_fj(params, type))

        if 'get'.__eq__(type):
            r = req.get(url, headers=header, params=params, name=api)
        else:
            r = req.post(url, headers=header, json=params, name=api)
        LogUtils.print_response(r, url_data.get('comment'))
        return r

    @staticmethod
    def send_req(type, url, params):
        '''调试用'''
        type = type.lower()
        header = DataUtils.get_user_info_auto()
        header.update(FanjiaoConfig.signature_fj(params, type))

        requests.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        if 'get'.__eq__(type):
            r = requests.get(url, headers=header, params=params, timeout=10)
        else:
            r = requests.post(url, headers=header, json=params, timeout=10)
        LogUtils.print_response(r, isformart=True)
        return r
