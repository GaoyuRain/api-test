# 测试环境 host：api_fj-idc.fanjiao.co
#
# 预发布环境 host：pre-api_fj.fanjiao.co
#
# 对外 api_fj 前缀：/walkman/api_fj
#
# 对内 api_fj 前缀：/walkman/internal/api_fj （对内接口需走 svc）
import hashlib
import json
from ast import literal_eval

from utils_fj.data_utils import DataUtils

# NewSalt = {"get": "MAaFS5Zc6ZIEapnmhurNyLLFwf3xWm", "post": "879f30c4b1641142c6192acc23cfb733"}


class FanjiaoConfig:

    @staticmethod
    def signature_fj(params, method='get', NewSalt="879f30c4b1641142c6192acc23cfb733"):
        if params is None:
            m = hashlib.md5(NewSalt.encode(encoding="utf-8"))
            return {'signature': m.hexdigest()}

        sign_params = params if isinstance(params, dict) else FanjiaoConfig.str_eval(params)
        # sign_keys = sorted(sign_params.keys())
        sort_str_list = []
        if method.lower() == "get":
            for key, values in sign_params.items():
                if isinstance(values, list):
                    for i in range(len(values)):
                        sort_str_list.append(key + "=" + str(values[i]))
                else:
                    sort_str_list.append(key + "=" + str(values))
            sign_str_list = sorted(sort_str_list)
            sign_str_new = '&'.join(sign_str_list)
            m = hashlib.md5((sign_str_new + NewSalt).encode(encoding="utf-8"))
        else:
            m = hashlib.md5((json.dumps(params) + NewSalt).encode(encoding="utf-8"))
        return {'signature': m.hexdigest()}

    @staticmethod
    def str_eval(obj_str):
        if isinstance(obj_str, str):
            try:
                r = literal_eval(obj_str)
                if isinstance(r, (int, float, bool)):
                    return obj_str
                else:
                    return r
            except Exception:
                return obj_str.strip()
        else:
            return obj_str


if __name__ == '__main__':
    # print(FanjiaoConfig.get_host('pro'))
    pass
