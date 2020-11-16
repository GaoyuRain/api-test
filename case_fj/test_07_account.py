"""
author :rain
Date : 2020/10/28
Description : 钱包
"""
import os

from locust import TaskSet, between, task, HttpUser

import constant
from utils_fj.api_utils import APIUtils
from utils_fj.locust_utils import LocustUtils


class TestAccount(TaskSet):

    def on_start(self):
        self.params_data = constant.account_api_data

    @task(1)
    def test_01_account_detail(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('account_detail'))

    @task(1)
    def test_02_account_rice_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('account_rice_list'))

    @task(1)
    def test_03_product_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('product_list'))

    @task(1)
    def test_04_pay_create_order(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('pay_create_order'))

    @task(1)
    def test_05_pay_apple_verify_receipt(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('pay_apple_verify_receipt'))

    @task(1)
    def test_06_account_consume_list(self):
        APIUtils.send_pre_req(self.client, self.params_data.get('account_consume_list'))


class WebsiteUser(HttpUser):
    host = constant.BASE_URL
    wait_time = between(5, 10)
    tasks = [TestAccount]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    LocustUtils.start_locust(file_name)
