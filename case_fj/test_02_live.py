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


class TestLive(TaskSet):

    @task(1)
    def test_01_gift_list(self):
        pass
        """礼物列表"""
        # r = LiveApi.get_gift_list()
        # data = dict(r.json()).get('data_fj')
        # print(data)
        # giftList: list = data.get('list')
        # print(len(giftList))
        # self.assertTrue(len(giftList) > 0)
        # for i in range(len(giftList)):
        #     self.assertIsNotNone(giftList[i].get('gift_id'))
        #     self.assertTrue(len(giftList[i].get('name')) > 0)
        #     self.assertTrue(giftList[i].get('rice') > 0)
        #     self.assertTrue(len(giftList[i].get('icon')) > 0)
        #     if giftList[i].get('duration') > 0:
        #         self.assertTrue(len(giftList[i].get('video_url')) > 0)


class WebsiteUser(HttpUser):
    host = constant.BASE_URL
    wait_time = between(5, 10)
    tasks = [TestLive]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    LocustUtils.start_locust(file_name)
