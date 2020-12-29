"""
author :rain
Date : 2020/07/20
Description :
"""
import unittest

from test_utils.api_utils import APIUtils
from test_utils.data_utils import DataUtils


class TestLive(unittest.TestCase):

    def setUp(self) -> None:
        self.url_data = DataUtils.get_yaml_data('t02_live_api_data.yaml')

    # @unittest.skip("直播暂时不可用")
    def test_01_gift_list(self):
        """礼物列表"""
        r = APIUtils.send_auto_request(self.url_data.get('gift_list'))
        data = dict(r.json()).get('data')
        print(data)
        giftList: list = data.get('list')
        print(len(giftList))
        self.assertTrue(len(giftList) > 0)
        for i in range(len(giftList)):
            self.assertIsNotNone(giftList[i].get('gift_id'))
            self.assertTrue(len(giftList[i].get('name')) > 0)
            self.assertTrue(giftList[i].get('rice') > 0)
            self.assertTrue(len(giftList[i].get('icon')) > 0)
            if giftList[i].get('duration') > 0:
                self.assertTrue(len(giftList[i].get('video_url')) > 0)

    def test_02_live_open_time(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_open_time'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data is not None
        assert len(data.get('start')) > 0
        assert len(data.get('end')) > 0
        assert len(data.get('now')) > 0
        assert (not data.get('is_open')) or (data.get('is_open'))
        assert data.get('remind_status') >= 0

    def test_03_live_open_remind(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_open_remind'))
        assert 200 == r.status_code
        message = r.json().get('message')
        assert 'OK'.__eq__(message)

    def test_04_live_background_add(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_background_add'))
        assert 200 == r.status_code
        message = r.json().get('message')
        assert 'OK'.__eq__(message)

    def test_05_live_background_del(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_background_del'))
        assert 200 == r.status_code
        message = r.json().get('message')
        assert 'OK'.__eq__(message)

    def test_06_live_backend(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_backend'))

        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        backgrounds: list = data.get('backgrounds')
        labels: list = data.get('labels')
        assert backgrounds is not None
        assert labels is not None
        attribute = 0
        for background in backgrounds:
            if attribute != 1:
                attribute = background.get('attribute')
            assert len(background.get('image')) > 0
        # 必须有预设背景图
        assert attribute == 1
        for label in labels:
            assert len(label.get('icon')) > 0
            assert len(label.get('name')) > 0

    def test_07_live_audience_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_audience_list'))
        assert 200 == r.status_code

    def test_08_live_audio_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_audio_list'))
        assert 200 == r.status_code

    def test_09_live_info(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_info'))
        assert 200 == r.status_code

    def test_10_live_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_list'))
        assert 200 == r.status_code

    def test_11_live_update(self):
        r = APIUtils.send_auto_request(self.url_data.get('live_update'))
        assert 200 == r.status_code

    def test_12_gift_current_ranking(self):
        r = APIUtils.send_auto_request(self.url_data.get('gift_current_ranking'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        uinfo = data.get('u_info')
        assert len(uinfo.get('avatar')) > 0
        assert len(uinfo.get('nickname')) > 0
        assert uinfo.get('uid') > 0
        assert uinfo.get('total_send_rice') >= 0

    # def test_13_gift_info(self):
    #     r = APIUtils.send_request(self.url_data.get('gift_info'))
    #     assert 200 == r.status_code

    def test_14_gift_top_ranking(self):
        r = APIUtils.send_auto_request(self.url_data.get('gift_top_ranking'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        uinfo = data.get('u_info')
        assert len(uinfo.get('avatar')) > 0
        assert len(uinfo.get('nickname')) > 0
        assert uinfo.get('uid') > 0
        assert uinfo.get('total_send_rice') >= 0

    def test_15_gift_user_live_ticket(self):
        r = APIUtils.send_auto_request(self.url_data.get('gift_user_live_ticket'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('ticket') >= 0
        assert data.get('today_ticket') >= 0
        assert data.get('total_ticket') >= 0

    @unittest.skip('404,暂时不确定有没有这个接口')
    def test_16_gift_user_ranking(self):
        r = APIUtils.send_auto_request(self.url_data.get('gift_user_ranking'))
        assert 200 == r.status_code


if __name__ == '__main__':
    unittest.main()
