'''
@Author: Yang
@Date: 2019-11-04 11:25:37
@LastEditors: Yang
@LastEditTime: 2019-11-11 15:39:54
@FilePath: /scrapyDemo/totorial/totorial/items.py
@Description:
'''
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    price = scrapy.Field()
    name = scrapy.Field()
    shop = scrapy.Field()
