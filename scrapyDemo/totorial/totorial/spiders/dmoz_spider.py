'''
@Author: Yang
@Date: 2019-11-04 13:24:46
@LastEditors: Yang
@LastEditTime: 2019-11-11 15:54:27
@FilePath: /scrapyDemo/totorial/totorial/spiders/dmoz_spider.py
@Description:
'''
from totorial.items import DmozItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import scrapy
from bs4 import BeautifulSoup
import re
"""


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc
"""


class MovieSpider(CrawlSpider):
    name = 'lamp'
    allowed_domains = ['jd.com']
    start_urls = [
        'https://search.jd.com/Search?keyword=%E5%90%B8%E9%A1%B6%E7%81%AF&enc=utf-8&suggest=1.his.0.0&wq=&pvid=66366f5ebbc248638aa6bc4eecae7867']
    # rules = (
    #     Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+.*'))),
    #     Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+')),
    #          callback='parse_item'),
    # )

    def parse(self, response):
        item = DmozItem()
        for quote in response.css('ul.gl-warp li'):
            item['name'] = quote.css('div.p-name em::text').getall(),
            item['price'] = quote.css('div.p-price i::text').getall(),
            item['shop'] = quote.css('div.p-shop a::attr(title)').getall()
            yield item

            # yield {
            #     'price': quote.css('div.p-price i::text').getall(),
            #     'name': quote.css('div.p-name em::text').getall(),
            #     'shop': quote.css('div.p-shop a::attr(title)').getall()
            # }

            # for quote in response.css('.v-fixed li'):
            #     yield {
            #         'type': quote.css('a::attr(title)').getall(),
            #     }
            # a1 = response.css('div.s-line')[0]
            # for quote in a1.css('ul.J_valueList li'):
            #     yield {
            #         'golv': quote.css('a::text').getall()
            #     }
            #     next_page = response.css('li.next a::attr("href")').get()
            #     if next_page is not None:
            #         yield response.follow(next_page, self.parse)
            # a2 = response.css('div.s-line')[1]
            # for quote in a2.css('ul.J_valueList li'):
            #     yield {
            #         'cct': quote.css('a::text').getall()
            #     }
            # a3 = response.css('div.s-line')[2]
            # for quote in a3.css('ul.J_valueList li'):
            #     yield {
            #         'dianya': quote.css('a::text').getall()
            #     }
