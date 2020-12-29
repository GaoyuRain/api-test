# """
# author :rain
# Date : 2020/08/12
# Description :
# """
# import json
# import os
#
# import requests
# import yaml
#
# from constant import get_verify_code_url, BASE_DIR
#
# user_info = []
#
#
# def login_setbirthday(zone, phone):
#     # 获取验证码
#     verify_url = '/user/verify_code'
#     verify_param = {
#         "zone": zone,
#         "phone": phone
#     }
#     data = {'zone': '+99', "phone": phone}
#     data['signature'] = signature_fj(data)
#     r = requests.get(get_verify_code_url, params=data)
#     print(r.json())
#
#     login_url = "/user/login"
#     login_data = {
#         "zone": zone,
#         "phone": phone,
#         "verify_code": "0000",
#         "device_type": 1,
#     }
#     r = requests.post(login_url, json.dumps(login_data))
#     jsondata = r.json()
#     print(jsondata)
#     # datas = jsondata.get('data_fj')
#     data = r.json()
#     login_token = data.get('data_fj').get('token')
#     uid = data.get('data_fj').get('user').get('uid')
#     nickname = data.get('data_fj').get('user').get('nickname')
#     avatar = data.get('data_fj').get('user').get('avatar')
#     uinfo = {'token': login_token, 'uid': uid, 'nickname': nickname, 'avatar': avatar}
#     global user_info
#     user_info.append(uinfo)
#
#     # data2 = {"birthday": "1975-07-21"}
#     # hs.post("http://test-api.fanjiao.co/walkman/api/user/update", data_fj=data2, headers=headers)
#
#
# def save_user_info():
#     file_path = BASE_DIR + os.sep + 'user_info.yaml'
#     with open(file_path, 'w', encoding='UTF-8') as f:
#         yaml.dump(user_info, f, allow_unicode=True, encoding='UTF-8')
#
#
# def create_data():
#     for i in range(910, 980):
#         phone = '19999999' + str(i)
#         login_setbirthday('99', phone)
#
#     save_user_info()
#
#
# def init():
#     file_path = BASE_DIR + os.sep + 'data_fj' + os.sep + 'user_info.yaml'
#     with open(file_path, 'r', encoding='UTF-8') as f:
#         global user_info
#         user_info = yaml.safe_load(f)
#         print('init:' + str(user_info))
#     return user_info
#
#
# def send_album_gift():
#     albumin = AlbumInfoAPI()
#     for user in user_info:
#         heasers = {'token': user.get('token')}
#         albumin.reward_buy(heasers)
#
#
# if __name__ == '__main__':
#     # create_data()
#     init()
#     # data_fj = []
#     # for i in range(len(user_info)):
#     #     data_fj.append(user_info[i].get('uid'))
#     # create_data()
#     # print(data_fj)
#     print(user_info)
#     send_album_gift()
