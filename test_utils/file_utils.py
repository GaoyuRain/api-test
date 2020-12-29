"""
author :rain
Date : 2020/07/20
Description :文件操作
"""
import os

from test_utils.data_utils import DataUtils
from test_utils.thread_utils import DownLoadThread
from constant import BASE_DIR


class FileUtils:

    @staticmethod
    def downdload_gift_icon():
        file_path = BASE_DIR + os.sep + 'data_fj' + os.sep + 'giftdata'
        FileUtils.clear_file(file_path)
        dataList = DataUtils.get_yaml_data('gift_list.yaml')
        # print(dataList)
        for i in range(len(dataList)):
            iconUrl = dataList[i].get('icon')
            fileName = file_path + os.sep + 'gift' + '_' + str(dataList[i].get('gift_id')) + '_' + dataList[i].get(
                'name') + '.png'
            DownLoadThread(iconUrl, fileName).start()

    @staticmethod
    def clear_file(file_path):
        """清空文件夹"""
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        fileList = os.listdir(file_path)
        # print(fileList)
        for i in range(len(fileList)):
            if fileList[i].endswith('.html'):
                os.remove(file_path + os.sep + fileList[i])


if __name__ == '__main__':
    FileUtils.downdload_gift_icon()
    # file_path = BASE_DIR + os.sep + 'data_fj' + os.sep + 'giftdata'
    # FileUtils.clear_file(file_path)
