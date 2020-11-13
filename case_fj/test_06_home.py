"""
author :rain
Date : 2020/10/28
Description : 首页
"""
import os
import subprocess

from locust import between, TaskSet, task, HttpUser

import constant
from base_fj.locust_config import LocustConfig, KILL_LOSUCT_CMD
from utils_fj.api_utils import APIUtils


class TestHome(TaskSet):

    def on_start(self):
        self.params_data = constant.home_api_data

    @task(1)
    def test_01_search_guide(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('search_guide'))

    @task(1)
    def test_02_search_keyword(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('search_keyword'))

    @task(1)
    def test_03_recommend_banner(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('recommend_banner'))

    @task(1)
    def test_04_recommend_major(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('recommend_major'))

    @task(1)
    def test_05_recommend_cv(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('recommend_cv'))

    @task(1)
    def test_06_recommend_category(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('recommend_category'))

    @task(1)
    def test_07_album_category(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('album_category'))

    @task(1)
    def test_08_recommend_home(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('recommend_home'))


class WebsiteUser(HttpUser):
    host = constant.BASE_URL
    wait_time = between(5, 10)
    tasks = [TestHome]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    print(LocustConfig.locust_cmd(file_name))
    # subprocess.call(KILL_LOSUCT_CMD, shell=True)
    subprocess.call(LocustConfig.locust_cmd(file_name), shell=True)
