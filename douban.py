'''
@Author: Yang
@Date: 2020-06-16 16:18:21
@LastEditors: Yang
@LastEditTime: 2020-06-18 13:59:52
@FilePath: /python学习/douban.py
@Description: 头部注释
'''

import requests
from bs4 import BeautifulSoup
import lxml
import json
import xlwt
import multiprocessing

n = 1


def main(url):
    header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              "Host": "movie.douban.com",
              "Referer": "https://movie.douban.com/top250?start=0&filter=",
              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    # url = 'https://movie.douban.com/top250?start=' + str(page*25)+'&filter='
    html = request_douban(url, header)
    soup = BeautifulSoup(html, 'lxml')
    # lists = soup.select('ol.grid_view li')
    # for item in lists:
    #     print(item.select('.hd span')[0].string)
    list = soup.find(class_='grid_view').find_all('li')
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影TOP250', cell_overwrite_ok=True)
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '图片')
    sheet.write(0, 2, '排名')
    sheet.write(0, 3, '评分')
    sheet.write(0, 4, '作者')
    sheet.write(0, 5, '简介')
    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        item_intr = item.find(class_='inq').string
        print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_img +
              ' | ' + item_score + ' | ' + item_author + ' | ' + item_intr)
        global n
        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_img)
        sheet.write(n, 2, item_index)
        sheet.write(n, 3, item_score)
        sheet.write(n, 4, item_author)
        sheet.write(n, 5, item_intr)
        n = n+1
    book.save(u'豆瓣最受欢迎的250部电影.xlsx')


def request_douban(url, header):
    try:
        response = requests.get(url=url, headers=header)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


#
if __name__ == "__main__":
    pool = multiprocessing.Pool(
        multiprocessing.cpu_count)  # 根据电脑的cpu内核数量创建相应的线程池
    urls = []
    for i in range(0, 10):
        url = 'https://movie.douban.com/top250?start=' + \
            str(i * 25) + '&filter='
        urls.append(url)
    pool.map(main, urls)
    pool.close()  # 让它不再创建进程
    pool.join()  # 为的是让进程池的进程执行完毕再结束
