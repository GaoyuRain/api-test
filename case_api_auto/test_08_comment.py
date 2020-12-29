"""
author :rain
Date : 2020/10/28
Description :
"""
import unittest

from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils


class TestComment(unittest.TestCase):

    def setUp(self) -> None:
        self.url_data = DataUtils.get_yaml_data('t08_comment_api_data.yaml')

    def test_01_comment_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('comment_list'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_02_comment_list_good(self):
        r = APIUtils.send_auto_request(self.url_data.get('comment_list_good'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_03_comment_detail(self):
        r = APIUtils.send_auto_request(self.url_data.get('comment_detail'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_04_comment_publish(self):
        r = APIUtils.send_auto_request(self.url_data.get('comment_publish'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_05_comment_like(self):
        r = APIUtils.send_auto_request(self.url_data.get('comment_like'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_06_comment_report(self):
        r = APIUtils.send_auto_request(self.url_data.get('comment_report'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_07_comment_delete(self):
        r = APIUtils.send_auto_request(self.url_data.get('comment_delete'))
        data = dict(r.json())
        assert 200 == r.status_code


if __name__ == '__main__':
    unittest.main()
