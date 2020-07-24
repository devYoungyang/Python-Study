'''
@Author: Yang
@Date: 2020-06-29 10:45:29
@LastEditors: Yang
@LastEditTime: 2020-06-29 11:18:17
@FilePath: /python学习/youdaoDict.py
@Description: 头部注释
'''

import requests
import time
import hashlib
import random
# def main():


def get_ts():
    ts = int(time.time()*1000)
    return ts


def get_bv():
    appVersion = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    m = hashlib.md5()
    m.update(appVersion.encode('utf-8'))
    bv = m.hexdigest()
    return bv


def get_salt(ts):
    num = int(random.random()*10)
    salt = str(ts)+str(num)
    return salt


def get_sign(salt):
    a = 'fanyideskweb'
    b = '你死定了'
    c = salt
    d = 'mmbP%A-r6U3Nw(n]BjuEU'
    str_data = a+b+str(c)+d
    m = hashlib.md5()
    m.update(str_data.encode('utf-8'))
    sign = m.hexdigest()
    return sign


def get_data_form():
    ts = get_ts()
    salt = get_salt(ts)
    form_data = {"i": "你死定了",
                 "from": "AUTO",
                 "to": "AUTO",
                 "smartresult": "dict",
                 "client": "fanyideskweb",
                 "salt": str(salt),
                 "sign": get_sign(salt),
                 "ts": str(ts),
                 "bv": get_bv(),
                 "doctype": "json",
                 "version": "2.1",
                 "keyfrom": "fanyi.web",
                 "action": "FY_BY_REALTlME", }
    return form_data


url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
header = {"Cookie": "OUTFOX_SEARCH_USER_ID=-753618449@10.168.1.247; OUTFOX_SEARCH_USER_ID_NCOO=101298913.63356031; JSESSIONID=aaaw1RZrZ6TwH8IDI69lx; ___rl__test__cookies=1593397920726",
          "Host": "fanyi.youdao.com",
          "Referer": "http://fanyi.youdao.com/",
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
data = {"i": "你死定了",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15933979207295",
        "sign": "751167fcd9a820f241eade65a6c3fe85",
        "ts": "1593397920729",
        "bv": "aa061c171a429ca520c4594fc212cef5",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME", }
response = requests.post(url=url, data=get_data_form(), headers=header)
print(response.content)
