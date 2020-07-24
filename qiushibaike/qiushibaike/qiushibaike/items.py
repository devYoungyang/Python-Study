'''
@Author: Yang
@Date: 2020-06-22 16:05:32
@LastEditors: Yang
@LastEditTime: 2020-07-01 13:14:44
@FilePath: /python学习/qiushibaike/qiushibaike/qiushibaike/items.py
@Description: 头部注释
'''
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QiushibaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    author = scrapy.Field()
