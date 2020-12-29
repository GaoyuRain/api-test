"""
author :rain
Date : 2020/10/28
Description :
"""
import os

from locust import between, TaskSet, task, HttpUser

import constant
from test_utils.api_utils import APIUtils
from test_utils.locust_utils import LocustUtils


class TestAlbumInfo(TaskSet):

    def on_start(self):
        self.params_data = constant.album_info_api_data

    @task(1)
    def test_01_album_info(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('album_info'))

    @task(1)
    def test_02_actor_cv(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('actor_cv'))

    @task(1)
    def test_03_album_audio(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('album_audio'))

    @task(1)
    def test_04_album_recommend(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('album_recommend'))

    @task(1)
    def test_05_buy_album(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('buy_album'))

    @task(1)
    def test_06_follow_album(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('follow_album'))

    @task(1)
    def test_07_album_history(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('album_history'))

    @task(1)
    def test_08_album_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('album_list'))

    @task(1)
    def test_09_reward_buy(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('reward_buy'))

    @task(1)
    def test_10_reward_rank(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('reward_rank'))


class WebsiteUser(HttpUser):
    host = constant.BASE_URL
    wait_time = between(5, 10)
    tasks = [TestAlbumInfo]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    LocustUtils.start_locust(file_name)
