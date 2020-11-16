import os
import subprocess

import requests
from locust import TaskSet, between, task, HttpUser

import constant
from base_fj.locust_config import LocustConfig, KILL_LOSUCT_CMD
from utils_fj.api_utils import APIUtils
from utils_fj.log_utils import LogUtils


class TestXmly(TaskSet):

    @task(1)
    def test_placeOrder(self):
        url_placeOrder = "/trade-v3/placeorderandmakepayment"
        payMethods = [{"payMode": "BALANCE", "accountType": "XICOIN", "subAccount": "IOS"}]
        context = {}
        placeOrder = {"domain": 1,
                      "context": context,
                      "returnUrl": "http://www.ximalaya.com",
                      "userId": 11238014,
                      "payMethods": str(payMethods),
                      "orderItems": "1010000100000360145",
                      "tradeType": 1,
                      "timestamp": "1604910786647"
                      }
        response = self.client.post(constant.UAT_BASE_URL+url_placeOrder, data=placeOrder, headers=constant.HEADER6)
        LogUtils.print_response(response, "下单并直接支付")


class WebsiteUser(HttpUser):
    host = constant.UAT_BASE_URL
    wait_time = between(5, 10)
    tasks = [TestXmly]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    print(LocustConfig.locust_cmd(file_name))
    subprocess.call(LocustConfig.locust_cmd(file_name, has_web=True), shell=True)
