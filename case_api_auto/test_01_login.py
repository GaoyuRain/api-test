"""
author :rain
Date : 2020/07/20
Description :
"""
import unittest

import allure

import constant
from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.url_data = DataUtils.get_yaml_data('t01_login_api_data.yaml')

    @allure.step(title="获取验证码")
    def test_01_get_verify_code(self):
        """获取验证码"""
        r = APIUtils.send_auto_request(self.url_data.get('user_verify_code'))
        data = dict(r.json())
        # assert 'OK' in data_fj.get('message')
        assert 200 == r.status_code

    # @pytest.mark.parametrize('phone, code, message', DataUtils.get_login_data())
    @allure.step(title="登录")
    def test_02_user_login(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_login'))
        data = dict(r.json())
        # assert 'OK' in data_fj.get('message')
        assert 200 == r.status_code

        userinfo = data.get('data')
        assert userinfo is not None
        if userinfo is not None:
            constant.user_info = None
            DataUtils.set_data(userinfo, constant.uinfo_api_auto_file)

    def test_03_user_login_wx(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_login_wx'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_04_user_tourist_login(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_tourist_login'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_05_user_wx_login(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_wx_login'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_06_user_wx_bind(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_wx_bind'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_07_user_wx_mini_login(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_wx_mini_login'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_08_user_wx_mini_bind(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_wx_mini_bind'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_09_user_apple_login(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_apple_login'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_10_user_apple_bind(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_apple_bind'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_11_user_third_unbind(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_third_unbind'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_12_user_update(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_update'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_13_user_update_phone(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_update_phone'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_14_user_update_wx(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_update_wx'))
        data = dict(r.json())
        assert 200 == r.status_code

    def test_15_user_update_apple(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_update_apple'))
        data = dict(r.json())
        assert data.get('message') is None
        assert 200 == r.status_code


if __name__ == '__main__':
    unittest.main()
