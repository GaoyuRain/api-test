"""
author :rain
Date : 2020/07/20
Description :
"""
from threading import Thread

import requests


class DownLoadThread(Thread):
    def __init__(self, url, filename):
        super().__init__()
        self.url = url
        self.filename = filename

    def run(self):
        # filename = self.url[self.url.rfind('/') + 1:]
        # file_path = BASE_DIR + os.sep + 'data_fj' + os.sep + 'giftdata' + os.sep + self.filename
        data = requests.get(self.url)
        with open(self.filename, 'wb') as file:
            file.write(data.content)


if __name__ == '__main__':
    print()
    pass
