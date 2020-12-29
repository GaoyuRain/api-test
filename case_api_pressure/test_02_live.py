"""
author :rain
Date : 2020/07/20
Description :
"""
import os

# from api_fj.live_api import LiveApi
from locust import TaskSet, between, task, HttpUser

import constant
from utils_fj.locust_utils import LocustUtils

import os

from locust import TaskSet, task, between, HttpUser

import constant
from utils_fj.api_utils import APIUtils
from utils_fj.locust_utils import LocustUtils


class TestLive(TaskSet):

    def on_start(self):
        self.params_data = constant.live_data

    @task(1)
    def test_01_gift_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('gift_list'))

    @task(1)
    def test_02_live_open_time(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_open_time'))

    @task(1)
    def test_03_live_open_remind(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_open_remind'))

    @task(1)
    def test_04_live_background_add(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_background_add'))

    @task(1)
    def test_05_live_background_del(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_background_del'))

    @task(1)
    def test_06_live_backend(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_backend'))

    @task(1)
    def test_07_live_audience_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_audience_list'))

    @task(1)
    def test_08_live_audio_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_audio_list'))

    @task(1)
    def test_09_live_info(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_info'))

    @task(1)
    def test_10_live_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_list'))

    @task(1)
    def test_11_live_update(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('live_update'))

    @task(1)
    def test_12_gift_current_ranking(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('gift_current_ranking'))

    @task(1)
    def test_14_gift_top_ranking(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('gift_top_ranking'))

    @task(1)
    def test_15_gift_user_live_ticket(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('gift_user_live_ticket'))


class WebsiteUser(HttpUser):
    host = constant.BASE_URL
    wait_time = between(5, 10)
    tasks = [TestLive]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    LocustUtils.start_locust(file_name)
