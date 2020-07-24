'''
@Author: Yang
@Date: 2020-07-03 10:14:55
@LastEditors: Yang
@LastEditTime: 2020-07-03 13:59:02
@FilePath: /python学习/download.py
@Description: 头部注释
'''
import requests


def download(url):

    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    }
    with open('123.jpg', 'wb') as f:
        img = requests.get(url, headers=header).content
        f.write(img)
    print(url)


download('http://img3.imgtn.bdimg.com/it/u=1428981598,4123167573&fm=26&gp=0.jpg')
