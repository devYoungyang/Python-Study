'''
@Author: Yang
@Date: 2020-06-22 16:05:32
@LastEditors: Yang
@LastEditTime: 2020-07-01 13:35:31
@FilePath: /python学习/qiushibaike/qiushibaike/qiushibaike/pipelines.py
@Description: 头部注释
'''
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import qiushibaike.database as db
import pymongo
from itemadapter import ItemAdapter


class QiushibaikePipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client['qiushibaike']
        self.coll = db['qiushi']

    def process_item(self, item, spider):
        self.coll.insert_one(item)
        # print(str(item) + '============')
        return item
