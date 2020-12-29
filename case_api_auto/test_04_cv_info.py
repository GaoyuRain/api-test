import unittest

from utils_fj.api_utils import APIUtils
from utils_fj.data_utils import DataUtils


class TestCvInfo(unittest.TestCase):

    def setUp(self) -> None:
        self.url_data = DataUtils.get_yaml_data('t04_cv_info_api_data.yaml')

    def test_01_cv_info(self):
        r = APIUtils.send_auto_request(self.url_data.get('cv_info'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert len(data.get('name')) > 0
        assert data.get('cv_id') is not None
        assert len(data.get('avatar')) > 0

    def test_02_album_cv_list(self):
        r = APIUtils.send_auto_request(self.url_data.get('album_cv_list'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('list') is not None

    def test_03_user_follow_cv(self):
        r = APIUtils.send_auto_request(self.url_data.get('user_follow_cv'))
        assert 200 == r.status_code

    def test_04_cv_attention(self):
        r = APIUtils.send_auto_request(self.url_data.get('cv_attention'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('list') is not None

    def test_05_cv_fans(self):
        r = APIUtils.send_auto_request(self.url_data.get('cv_fans'))
        assert 200 == r.status_code
        data: dict = dict(r.json()).get('data')
        assert data.get('list') is not None


if __name__ == '__main__':
    unittest.main()
