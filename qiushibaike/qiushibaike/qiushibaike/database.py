'''
@Author: Yang
@Date: 2020-06-30 14:30:26
@LastEditors: Yang
@LastEditTime: 2020-06-30 16:00:08
@FilePath: /python学习/qiushibaike/qiushibaike/qiushibaike/database.py
@Description: 头部注释
'''


import pymysql

MYSQL_DB = 'yang'
MYSQL_USER = 'root'
MYSQL_PASS = '12345678'
MYSQL_HOST = 'localhost'

connection = pymysql.connect(host=MYSQL_HOST,
                             user=MYSQL_USER,
                             password=MYSQL_PASS,
                             db=MYSQL_DB,
                             cursorclass=pymysql.cursors.DictCursor)
