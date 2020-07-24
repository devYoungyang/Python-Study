'''
@Author: Yang
@Date: 2020-06-24 14:45:37
@LastEditors: Yang
@LastEditTime: 2020-06-24 14:55:15
@FilePath: /python学习/index.py
@Description: 头部注释
'''
import requests
from requests_html import HTMLSession
from requests_file import FileAdapter

session = HTMLSession()
session.mount('file://', FileAdapter())
html = session.get(f'file:///Users/yang/Desktop/python学习/index.html')
print(html.text)
