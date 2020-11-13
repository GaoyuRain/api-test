"""
author :rain
Date : 2020/07/17
Description :
"""

import curlify
import requests

# 工程根目录
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
from utils_fj.data_utils import DataUtils


class CurlDataUtils:

    @staticmethod
    def get_curl_command1(type, *data):
        '''
        :param type: 接口类型 get post
        :param data: url ,params
        :return:
        '''
        datas: dict = DataUtils.get_yaml_data('curl_model.yaml')
        # print(datas)
        typedata: str = datas.get(type)
        if type == 'post':
            url, params = data
            command = typedata.format(url, params)
        else:
            url = data[0]
            command = typedata.format(url)
        print(command)
        return command

    @staticmethod
    def get_curl_command(req: requests):
        # print(url)
        # r = requests.post(url, json.dumps(send_gift_params))
        # print(CurlDataUtils.get_curl_command(r.request))
        return curlify.to_curl(req)


if __name__ == '__main__':
    send_gift_url = '/gift/send'
    send_gift_params = """{"gift_id": 1, "count": 1, "from_uid": 1000049, "to_uid": 1009, "rice": 12}"""
    rice_ticket_url = '/gift/user/rice_ticket?uid=1009'
    CurlDataUtils.get_curl_command1('post', send_gift_url, send_gift_params)
    CurlDataUtils.get_curl_command1('get', rice_ticket_url)
