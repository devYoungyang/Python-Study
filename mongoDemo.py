'''
@Author: Yang
@Date: 2020-06-30 16:43:12
@LastEditors: Yang
@LastEditTime: 2020-07-01 10:02:12
@FilePath: /python学习/mongoDemo.py
@Description: 头部注释
'''
import pymongo

# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
myclient = pymongo.MongoClient(host='localhost', port=27017)
mydb = myclient['Students']
mycol = mydb['sites']
mydict = {'name': 'TOM', 'sex': 'man', 'height': '178'}
mycol.insert_one(mydict)
lists = myclient.list_database_names()
print(lists)
