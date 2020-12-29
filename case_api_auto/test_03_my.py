"""
author :rain
Date : 2020/10/28
Description :我的页面
"""
import unittest

from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils


class TestMy(unittest.TestCase):

    def setUp(self) -> None:
        self.url_data = DataUtils.get_yaml_data('t03_my_api_data.yaml')

    def test_01_user_info(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_info'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert len(data.get('avatar')) > 0
        assert len(data.get('nickname')) > 0
        assert len(data.get('phone')) > 0

    def test_02_attention_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_attention_list'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('list') is not None

    def test_03_user_fans(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_fans'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('list') is not None

    def test_04_user_my_flow(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_my_flow'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('follow_album_list') is not None

    def test_05_user_flow_albumlist(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_flow_albumlist'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('list') is not None

    def test_06_user_not_read(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_not_read'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data is not None

    def test_07_user_notice(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_notice'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('list') is not None

    def test_08_user_activity(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_activity'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('list') is not None

    def test_09_user_read_album(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_read_album'))
        assert 200 == r.status_code

    def test_10_user_purchase_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_purchase_list'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('list') is not None

    def test_11_follow_user(self):
        r = APIUtils.send_auto_request(self.url_data.get('follow_user'))
        assert 200 == r.status_code

    def test_13_user_permission(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_permission'))
        assert 200 == r.status_code


if __name__ == '__main__':
    unittest.main()
