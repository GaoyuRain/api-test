"""
author :rain
Date : 2020/10/28
Description : 钱包
"""

import unittest

from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils


class TestAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.url_data = DataUtils.get_yaml_data('t07_account_api_data.yaml')

    def test_01_account_detail(self):
        r = APIUtils.send_auto_request(self.url_data.get('account_detail'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_02_account_rice_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('account_rice_list'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_03_product_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('product_list'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_04_pay_create_order(self):
        r = APIUtils.send_auto_request(self.url_data.get('pay_create_order'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_05_pay_apple_verify_receipt(self):
        r = APIUtils.send_auto_request(self.url_data.get('pay_apple_verify_receipt'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_06_account_consume_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('account_consume_list'))
        data = dict(r.json())
        assert 200 == r.status_code


if __name__ == '__main__':
    unittest.main()
