"""
author :rain
Date : 2020/10/28
Description :我的页面
"""
import os
import subprocess

from locust import TaskSet, task, between, HttpUser

import constant
from base_fj.locust_config import LocustConfig, KILL_LOSUCT_CMD
from utils_fj.api_utils import APIUtils


class TestMy(TaskSet):

    def on_start(self):
        self.params_data = constant.my_api_data

    @task(1)
    def test_01_user_info(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_info'))

    @task(1)
    def test_02_attention_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_attention_list'))

    @task(1)
    def test_03_user_fans(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_fans'))

    @task(1)
    def test_04_user_my_flow(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_my_flow'))

    @task(1)
    def test_05_user_flow_albumlist(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_flow_albumlist'))

    @task(1)
    def test_06_user_not_read(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_not_read'))

    @task(1)
    def test_07_user_notice(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_notice'))

    @task(1)
    def test_08_user_activity(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_activity'))

    @task(1)
    def test_09_user_read_album(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_read_album'))

    @task(1)
    def test_10_user_purchase_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_purchase_list'))

    @task(1)
    def test_11_follow_user(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('follow_user'))


class WebsiteUser(HttpUser):
    host = constant.BASE_URL
    wait_time = between(5, 10)
    tasks = [TestMy]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    print(LocustConfig.locust_cmd(file_name))
    subprocess.call(KILL_LOSUCT_CMD, shell=True)
    subprocess.call(LocustConfig.locust_cmd(file_name), shell=True)
