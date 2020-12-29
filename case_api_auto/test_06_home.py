"""
author :rain
Date : 2020/10/28
Description : 首页
"""

import unittest

from test_utils.api_utils import APIUtils
from test_utils.data_utils import DataUtils


class TestHome(unittest.TestCase):

    def setUp(self) -> None:
        self.url_data = DataUtils.get_yaml_data('t06_home_api_data.yaml')

    def test_01_search_guide(self):
        r = APIUtils.send_auto_request(self.url_data.get('search_guide'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_02_search_keyword(self):
        r = APIUtils.send_auto_request(self.url_data.get('search_keyword'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_03_recommend_banner(self):
        r = APIUtils.send_auto_request(self.url_data.get('recommend_banner'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_04_recommend_major(self):
        r = APIUtils.send_auto_request(self.url_data.get('recommend_major'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_05_recommend_cv(self):
        r = APIUtils.send_auto_request(self.url_data.get('recommend_cv'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_06_recommend_category(self):
        r = APIUtils.send_auto_request(self.url_data.get('recommend_category'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_07_album_category(self):
        r = APIUtils.send_auto_request(self.url_data.get('album_category'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_08_recommend_home(self):
        r = APIUtils.send_auto_request(self.url_data.get('recommend_home'))
        data = dict(r.json())
        assert 200 == r.status_code


if __name__ == '__main__':
    unittest.main()
