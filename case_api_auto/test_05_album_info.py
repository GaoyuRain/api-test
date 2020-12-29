"""
author :rain
Date : 2020/10/28
Description :
"""
import unittest

from test_utils.api_utils import APIUtils
from test_utils.data_utils import DataUtils


class TestAlbumInfo(unittest.TestCase):

    def setUp(self) -> None:
        self.url_data = DataUtils.get_yaml_data('t05_album_info_api_data.yaml')

    def test_01_album_info(self):
        r = APIUtils.send_auto_request(self.url_data.get('album_info'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert len(data.get('name')) > 0
        assert data.get('album_id') is not None
        assert len(data.get('cover')) > 0

    def test_02_actor_cv(self):
        r = APIUtils.send_auto_request(self.url_data.get('actor_cv'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        cv_list: list = data.get('cv_list')
        assert cv_list is not None
        if cv_list.__len__() > 0:
            for cv in cv_list:
                assert len(cv.get('name')) > 0
                assert len(cv.get('role_name')) > 0
                assert cv.get('cv_id') > 0

    def test_03_album_audio(self):
        r = APIUtils.send_auto_request(self.url_data.get('album_audio'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        audios_list: list = data.get('audios_list')
        assert audios_list is not None
        if audios_list.__len__() > 0:
            for audio in audios_list:
                assert len(audio.get('name')) > 0
                assert len(audio.get('description')) > 0
                assert len(audio.get('cover')) > 0
                assert len(audio.get('src')) > 0
                assert audio.get('audio_id') > 0

    def test_04_album_recommend(self):
        r = APIUtils.send_auto_request(self.url_data.get('album_recommend'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        rec_list: list = data.get('rec_list')
        assert rec_list is not None
        if rec_list.__len__() > 0:
            for rec in rec_list:
                assert len(rec.get('name')) > 0
                assert len(rec.get('description')) > 0
                assert len(rec.get('cover')) > 0
                assert len(rec.get('author_name')) > 0
                assert rec.get('album_id') > 0

    def test_05_buy_album(self):
        r = APIUtils.send_auto_request(self.url_data.get('buy_album'))
        assert 200 == r.status_code
        message: dict = dict(r.json()).get('message')
        assert len(message) > 0

    def test_06_follow_album(self):
        r = APIUtils.send_auto_request(self.url_data.get('follow_album'))
        assert 200 == r.status_code
        message: dict = dict(r.json()).get('message')
        assert len(message) > 0

    def test_07_album_history(self):
        r = APIUtils.send_auto_request(self.url_data.get('album_history'))
        assert 200 == r.status_code
        message: dict = dict(r.json()).get('message')
        assert len(message) > 0

    def test_08_album_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('album_list'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        album_list: list = data.get('list')
        assert album_list is not None
        if album_list.__len__() > 0:
            for cv in album_list:
                assert len(cv.get('name')) > 0
                assert len(cv.get('cover')) > 0
                assert cv.get('album_id') > 0
                assert cv.get('price') > 0
                assert cv.get('ori_price') > 0

    def test_09_reward_buy(self):
        r = APIUtils.send_auto_request(self.url_data.get('reward_buy'))
        assert 200 == r.status_code
        message: dict = dict(r.json()).get('message')
        assert len(message) > 0

    def test_10_reward_rank(self):
        r = APIUtils.send_auto_request(self.url_data.get('reward_rank'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        rank_list: list = data.get('rank')
        assert rank_list is not None
        if len(rank_list) > 0:
            for rank in rank_list:
                assert len(rank.get('nickname')) > 0
                assert len(rank.get('avatar')) > 0
                assert rank.get('uid') > 0
                assert rank.get('total_rice') > 0


if __name__ == '__main__':
    unittest.main()
