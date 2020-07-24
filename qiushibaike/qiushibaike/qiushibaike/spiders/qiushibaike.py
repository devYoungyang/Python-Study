'''
    @Author: Yang
    @Date: 2019-10-11 13:31:19
@LastEditors: Yang
@LastEditTime: 2020-07-01 13:30:01
@FilePath: /python学习/qiushibaike/qiushibaike/qiushibaike/spiders/qiushibaike.py
    @Description: 头部注释
    '''


import scrapy
from qiushibaike.items import QiushibaikeItem


class QiushiSpider(scrapy.Spider):
    name = 'qiushibaike'
    headers = {
        "Host": "www.qiushibaike.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }

    def start_requests(self):
        urls = [
            'https://www.qiushibaike.com/8hr/page/1/',
            'https://www.qiushibaike.com/8hr/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        # page = response.url.split('/')[-2]
        # filename = 'qiushi-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('saved file %s' % filename)

        for item in response.css('.recommend-article li'):
            # qbItem = QiushibaikeItem()
            # qbItem['title'] = item.css(
            #     'div.recmd-right a.recmd-content::text').get(),
            # qbItem['author'] = item.css(
            #     'div.recmd-right span.recmd-name::text').get(),
            # yield qbItem
            yield {
                'title': item.css('div.recmd-right a.recmd-content::text').get(),
                'author': item.css('div.recmd-right span.recmd-name::text').get(),
            }
