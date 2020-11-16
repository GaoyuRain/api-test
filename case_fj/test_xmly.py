import json
import os
import subprocess

from locust import TaskSet, between, task, HttpUser

from base_fj.locust_config import LocustConfig
from constant import UAT_BASE_URL, HEADER6, TEST_BASE_URL, HEADER1
from utils_fj.log_utils import LogUtils


class TestXmly(TaskSet):

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
        LogUtils.print_response(response, '支付接口')

    @task(1)
    def get_myOrderAll(self):
        url_Order = "/trade/order/all"
        response = self.client.get(url_Order, headers=HEADER1, verify=False)
        LogUtils.print_response(response, '我的订单-全部')

    @task(1)
    def get_myOrderPaying(self):
        url_Order = "/trade/order/paying"
        response = self.client.get(url_Order, headers=HEADER1, verify=False)
        LogUtils.print_response(response, '我的订单-待付款')

    @task(1)
    def get_myOrderUndelivered(self):
        url_Order = "/trade/order/undelivered"
        response = self.client.get(url_Order, headers=HEADER1, verify=False)
        LogUtils.print_response(response, '我的订单-待发货')

    @task(1)
    def get_myOrderhip(self):
        url_Order = "/trade/order/ship"
        response = self.client.get(url_Order, headers=HEADER1, verify=False)
        LogUtils.print_response(response, '我的订单-待收货')

    @task(1)
    def get_myOrderFinished(self):
        url_Order = "/trade/order/finished"
        response = self.client.get(url_Order, headers=HEADER1, verify=False)
        LogUtils.print_response(response, '我的订单-已完成')

    @task(1)
    def get_myOrderPrePay(self):
        url_Order = "/trade/order/prePay/202011164001864000047265766"
        response = self.client.get(url_Order, headers=HEADER1, verify=False)
        LogUtils.print_response(response, '我的订单-立即支付前置')





class WebsiteUser(HttpUser):
    host = TEST_BASE_URL
    wait_time = between(5, 10)
    tasks = [TestXmly]


if __name__ == '__main__':
    file_name = os.path.basename(__file__)
    print(LocustConfig.locust_cmd(file_name))
    # subprocess.call(KILL_LOSUCT_CMD, shell=True)
    subprocess.call(LocustConfig.locust_cmd(file_name, has_web=True), shell=True)
