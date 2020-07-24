'''
@Author: Yang
@Date: 2020-06-16 17:03:43
@LastEditors: Yang
@LastEditTime: 2020-07-10 14:47:49
@FilePath: /python学习/demo.py
@Description: 头部注释
'''
from bs4 import BeautifulSoup


html_doc = """
    <html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.title.string)
print(soup.find(class_='story').find_all('a', id='link2')[0].get_text())
print(soup.find(class_='story').find_all('a', id='link3')[0].get('href'))
print(soup.select('#link3')[0].get('href'))

# print(soup.prettify())


def header(referer):

    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }

    return headers
