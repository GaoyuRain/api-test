import json
import os
import subprocess

from locust import TaskSet, between, task, HttpUser

from base_fj.locust_config import LocustConfig
from constant import UAT_BASE_URL, HEADER6, TEST_BASE_URL, HEADER1
from utils_fj.log_utils import LogUtils


class TestTrade(TaskSet):

    @task
    def get_placeOrder(self):
        context = {}
        url_placeOrder = "/trade-v3/placeorderandmakepayment"
        placeOrder = {"domain": 1,
                      "context": context,
                      "returnUrl": "http://www.ximalaya.com",
                      "userId": 11238014,
                      "payMethods": '''[{"payMode": "BALANCE", "accountType": "XICOIN", "subAccount": "IOS"}]''',
                      "orderItems": "1010000100000360145",
                      "tradeType": 1,
                      "timestamp": "1604910786647"}
        response = self.client.post(url_placeOrder, data=placeOrder, headers=HEADER6, verify=False)
        LogUtils.print_response(response, 'UAT下单并直接支付接口')





class WebsiteUser(HttpUser):
    host = UAT_BASE_URL
    wait_time = between(5, 10)
    tasks = [TestTrade]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    print(LocustConfig.locust_cmd(file_name))
    # subprocess.call(KILL_LOSUCT_CMD, shell=True)
    subprocess.call(LocustConfig.locust_cmd(file_name, has_web=True), shell=True)
