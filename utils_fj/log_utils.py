"""
author :rain
Date : 2020/10/27
Description :
"""
import json

from requests import Response

import constant


class LogUtils:
    @staticmethod
    def print_response(r: Response, comment=None):
        if constant.hasLog:
            if comment is not None:
                print(f'接口: {comment}')
            print(f'CODE: {r.status_code}')
            print(f'URL: {r.url}')
            print(f'RESULT: {json.dumps(r.json(), ensure_ascii=False)}')
            print('-' * 100)
