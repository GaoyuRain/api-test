"""author :rainDate : 2020/07/17Description :测试数据"""import osimport randomimport yamlfrom constant import BASE_DIRimport constantclass DataUtils:    @staticmethod    def get_yaml_data(file_name):        print(file_name)        file_path = BASE_DIR + os.sep + 'data_fj' + os.sep + file_name        # print(file_path)        with open(file_path, 'r') as f:            return yaml.safe_load(f)    @staticmethod    def set_data(data, filename):        file_path = BASE_DIR + os.sep + 'data_fj' + os.sep + filename        with open(file_path, 'w', encoding='UTF-8') as f:            yaml.dump(data, f, allow_unicode=True, encoding='UTF-8')    @staticmethod    def set_user_info(data):        """写入用户信息"""        file_path = BASE_DIR + os.sep + 'data_fj' + os.sep + 'gift_list.yaml'        with open(file_path, 'w', encoding='UTF-8') as f:            yaml.dump(data.get('data_fj').get('list'), f, allow_unicode=True, encoding='UTF-8')    @staticmethod    def get_user_info(param="token"):        """获取用户信息"""        if constant.user_info is not None:            token = random.choice(constant.user_info).get(param)        else:            print('none')            data = DataUtils.get_yaml_data(constant.user_info_file)            token = random.choice(data).get(param)            constant.user_info = data        return {"token": token}    @staticmethod    def get_login_data():        data = DataUtils.get_yaml_data('t01_login_api_data.yaml')        data1 = data.values()        return [x.values() for x in data1]if __name__ == '__main__':    # DataUtils.set_gift_list_data()    # print(DataUtils.get_user_info())    # print(DataUtils.get_login_data()    # print(constant.home_api_data)    # DataUtils.init_params_data()    pass