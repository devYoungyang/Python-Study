'''
@Author: Yang
@Date: 2020-07-03 13:36:04
@LastEditors: Yang
@LastEditTime: 2020-07-10 14:48:47
@FilePath: /python学习/meizi.py
@Description: 头部注释
'''
# from multiprocessing import Pool
# from multiprocessing import Process
import multiprocessing
import concurrent
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import lxml
import os
from lxml import etree


def getProxy():
    return {
        'https': 'https://58.218.92.198:3660',
    }


def getHeaders():
    return {
        "referer": "https://www.mzitu.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }


def requests_page(url):
    try:
        response = requests.get(
            url=url, headers=getHeaders(), proxies=getProxy())
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def getImgUrls(page):
    baseUrl = 'https://www.mzitu.com/page/{}'.format(page)
    html = requests_page(baseUrl)
    # print(html.text)
    soup = BeautifulSoup(html, 'lxml')
    lists = soup.find('ul', id='pins').find_all('li')
    urls = []
    for item in lists:
        url = item.find('a').get('href')
        urls.append(url)
    return urls


def download(url):
    html = requests_page(url)
    print(url)
    soup = BeautifulSoup(html, 'lxml')
    page = soup.find('div', class_='pagenavi').find_all(
        'a')[-2].find('span').string
    title = soup.find('h2').string
    imgUrl_list = []
    for i in range(int(page)):
        url1 = url+'/{}'.format(i+1)
        html = requests.get(url=url1, headers=getHeaders(), proxies=getProxy())
        # subSoup = BeautifulSoup(html.text, 'lxml')
        root = etree.HTML(html.text)
        # print(response.text)
        imgUrl = root.xpath('//div[@class="main-image"]//img/@src')
        # imgUrl = subSoup.find('main-image').find('img').get('src')
        print(imgUrl)
        imgUrl_list.append(imgUrl)
    # print(imgUrl_list, title)
    downloadImg(imgUrl_list, title)


def downloadImg(img_url_list, title):
    print(img_url_list)
    os.mkdir(title)
    os.chdir(title)
    i = 1
    for item in img_url_list:
        fileName = '%s_%s.jpg' % (title, i)
        print('downloading....%s : NO.%s' % (title, str(i)))
        with open(fileName, 'wb') as f:
            img = requests.get(url=item, headers=getHeaders(),
                               proxies=getProxy()).content
            f.write(img)
        i += 1


def download_all_img(urls):

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as exector:
        for url in urls:
            exector.submit(download, url)
    # with Pool(5) as p:
    #     p.map(download, urls)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(download, urls)
    pool.close()
    pool.join()
    # for url in urls:
    #     download(url)


if __name__ == "__main__":
    img_urls = getImgUrls(1)
    print(img_urls)
    download_all_img(img_urls)
