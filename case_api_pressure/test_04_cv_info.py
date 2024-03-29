import os

from locust import TaskSet, task, between, HttpUser

import constant
from test_utils.api_utils import APIUtils
from test_utils.locust_utils import LocustUtils


class TestCvInfo(TaskSet):

    def on_start(self):
        self.params_data = constant.cv_info_api_data

    @task(1)
    def test_01_cv_info(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('cv_info'))

    @task(1)
    def test_02_album_cv_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('album_cv_list'))

    @task(1)
    def test_03_user_follow_cv(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('user_follow_cv'))

    @task(1)
    def test_04_cv_attention(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('cv_attention'))

    @task(1)
    def test_05_cv_fans(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('cv_fans'))


class WebsiteUser(HttpUser):
    host = constant.BASE_URL
    wait_time = between(5, 10)
    tasks = [TestCvInfo]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    LocustUtils.start_locust(file_name)
