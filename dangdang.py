'''
@Author: Yang
@Date: 2020-06-15 13:48:53
@LastEditors: Yang
@LastEditTime: 2020-07-02 16:14:10
@FilePath: /python学习/dangdang.py
@Description: 头部注释
'''
import requests
import re
import json
from bs4 import BeautifulSoup
import pymongo
from lxml import etree


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + \
        str(page)
    html = request_dangdang(url)
    lists = parse_result_etree(html)
    # lists = parse_result(html)
    write_data(lists)
    # for item in lists:
    # print(item)
    # write_item_to_file(item)


def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result_etree(html):
    root = etree.HTML(html)
    lists = root.xpath("//ul[@class='bang_list clearfix bang_list_mode']/li")
    for item in lists:
        title = item.xpath('div[@class="name"]/a/text()')[0]
        author = item.xpath('div[@class="publisher_info"][1]/a/text()')[0]
        publisher = item.xpath('div[@class="publisher_info"][2]/a/text()')[0]
        price = item.xpath('//span[@class="price_n"]/text()')[0]
        star = item.xpath('//span[@class="level"]/span/@style')[0]
        print(title, author, publisher, price, star)
        yield {
            'title': title,
            'author': author,
            'publisher': publisher,
            'price': price,
            'star': star
        }


def parse_result(html):
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    lists = soup.find('ul', class_='bang_list_mode').find_all('li')
    for item in lists:
        title = item.find(class_='name').find('a').get('title')
        author = item.find_all(class_='publisher_info')[
            0].find_all('a')[0].get_text()
        publisher = item.find_all(class_='publisher_info')[1].find('a').string
        price = item.find(class_='price').find(
            'span', class_='price_n').get_text()
        star = item.find(class_='level').find('span').get('style')
        print(title, author, publisher)
        yield {
            'title': title,
            'author': author,
            'publisher': publisher,
            'price': price,
            'star': star
        }
        # items = []
        # yield items
        # def parse_result(html):
        #     pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
        #     items = re.findall(pattern, html)
        #     for item in items:
        #         yield {
        #             'range': item[0],
        #             'iamge': item[1],
        #             'title': item[2],
        #             'recommend': item[3],
        #             'author': item[4],
        #             'times': item[5],
        #             'price': item[6]
        #         }

        # def write_item_to_file(item):
        #     # print('开始写入数据 ====> ' + str(item))
        #     with open('book.txt', 'a', encoding='UTF-8') as f:
        #         f.write(json.dumps(item, ensure_ascii=False) + '\n')
        #         f.close()


def write_data(data):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['dangdangwang']
    coll = db['books']
    coll.insert_many(data)
    print(data)


if __name__ == "__main__":
    for i in range(1, 10):
        main(i)
