"""
author :rain
Date : 2020/10/28
Description :
"""
import os

from locust import between, TaskSet, task, HttpUser

import constant
from utils_fj.api_utils import APIUtils
from utils_fj.locust_utils import LocustUtils


class TestComment(TaskSet):

    def on_start(self):
        self.params_data = constant.comment_api_data

    @task(1)
    def test_01_comment_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('comment_list'))

    @task(1)
    def test_02_comment_list_good(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('comment_list_good'))

    @task(1)
    def test_03_comment_detail(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('comment_detail'))

    @task(1)
    def test_04_comment_publish(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('comment_publish'))

    @task(1)
    def test_05_comment_like(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('comment_like'))

    @task(1)
    def test_06_comment_report(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('comment_report'))

    @task(1)
    def test_07_comment_delete(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('comment_delete'))


class WebsiteUser(HttpUser):
    host = constant.BASE_URL
    wait_time = between(5, 10)
    tasks = [TestComment]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    LocustUtils.start_locust(file_name)
