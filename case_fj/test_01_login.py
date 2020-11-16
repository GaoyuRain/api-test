"""
author :rain
Date : 2020/07/20
Description :
"""
import os

from locust import TaskSet, between, task, HttpUser

import constant
from utils_fj.api_utils import APIUtils
from utils_fj.locust_utils import LocustUtils


class TestLogin(TaskSet):

    def on_start(self):
        self.params_data = constant.login_api_data

    @task(1)
    def test_01_get_verify_code(self):
        """获取验证码"""
        # url_data = self.params_data.get('user_verify_code')
        # url = url_data.get('url')
        # params = url_data.get('params')
        # type = url_data.get('type')
        # header = FanjiaoConfig.signature_fj(params, type)
        # header.update(self.token)
        # r = self.client.get(url, params=params, headers=header, name=url)
        # LogUtils.print_response(r, url_data.get('comment'))
        APIUtils.send_pre_req(self.client, self.params_data.get('user_verify_code'))

    @task(1)
    def test_02_user_login(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_login'))

    @task(1)
    def test_03_user_login_wx(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_login_wx'))

    @task(1)
    def test_04_user_tourist_login(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_tourist_login'))

    @task(1)
    def test_05_user_wx_login(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_wx_login'))

    @task(1)
    def test_06_user_wx_bind(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_wx_bind'))

    @task(1)
    def test_07_user_wx_mini_login(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_wx_mini_login'))

    @task(1)
    def test_08_user_wx_mini_bind(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_wx_mini_bind'))

    @task(1)
    def test_09_user_apple_login(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_apple_login'))

    @task(1)
    def test_10_user_apple_bind(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_apple_bind'))

    @task(1)
    def test_11_user_third_unbind(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_third_unbind'))

    @task(1)
    def test_12_user_update(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_update'))

    @task(1)
    def test_13_user_update_phone(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_update_phone'))

    @task(1)
    def test_14_user_update_wx(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_update_wx'))

    @task(1)
    def test_15_user_update_apple(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_update_apple'))


class WebsiteUser(HttpUser):
    host = constant.BASE_URL
    wait_time = between(5, 10)
    tasks = [TestLogin]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    LocustUtils.start_locust(file_name)
