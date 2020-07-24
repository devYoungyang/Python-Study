'''
@Author: your name
@Date: 2019-10-11 13:31:19
@LastEditTime: 2020-06-17 10:10:12
@LastEditors: Yang
@Description: In User Settings Edit
@FilePath: /python学习/study.py
'''
#!/usr/bin/env python


import sys
import requests
from requests import Request, Session
# from operator import *

# abs(-6)  # 取绝对值


# all([1, 0, 3, 6])  # 返回false 有零，不是所有元素都为真

# any([0, 1, 2, 3])  # True，至少有一个元素为真

# bin(10)  # 十进制转换成二进制
# oct(10)  # 十进制转转八进制
# hex(20)  # 十进制转十六进制

# bool([1, 2, 3])  # 测试对象是否为真

# chr(66)  # 十进制转ASCII


# class Student():
#     def __init__(self, ids, name):
#         self.ids = ids
#         self.name = name

#     @classmethod
#     def f(cls):
#         print(cls)


# s = Student('11', '22')
# Student.f()

# # s = "print('Hello World')"

# # r = compile(s, '<string>', 'exec')
# # exec(r)

# c = complex(1, 2)   # 复数
# print(c)

# dir(s)  # 查看对象所有的方法

# divmod(10, 3)  # 取商取余

# ob = ['one', 'two', 'tree', 'four']
# for i, v in enumerate(ob):      # 枚举对象
#     print(i, v)

# t = '1+4+5'
# print(eval(t))  # 计算表达式
# b = sys.getsizeof(ob)  # 查看对象占用的字节数
# print(b)

# filter(lambda x: x > 4, [1, 2, 3, 5, 6, 7])  # 过滤器

# print('I am {0}, age {1}'.format('TOM', 22))

# frozenset([1, 2, 3, 4])  # 不可修改的集合

# getattr(s, 'name')   # 获取实例属性值

# hasattr(s, 'name')  # 是否有这个属性

# hash(s)  # 返回对象的哈希值

# id(s)  # 返回对象的内存地址

# help(s)  # 返回对象的帮助文档
# a = [1, 4, 3, 2, 1]
# sorted(a, reverse=True)

# b = [{'name': 'tom', 'age': 17, 'gender': 'male'}, {
#     'name': 'jerry', 'age': 22, 'gender': 'female'}]

# sorted(a, lambda x: x['age'], reverse=False)
# x = [1, 2, 3, 4]
# y = [4, 5, 6]
# list(zip(y, x))
# list('qwertyu')

# # gaobal 声明全局变量


# def calculator(a, b, k):
#     return {'+': add, '-': sub, '*': mul, '/': truediv, '**': pow}[k](a, b)


# calculator(1, 2, '+')

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d*%d=%d' % (j, i, j*i), end="\t")
#     print()

# request = requests.get('https://api.github.com/repos/psf/requests')
# print(request.json())

# session = requests.Session()
# session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# r = session.get('https://httpbin.org/cookies')
# print(r.text)
# print(r.headers)
# Request('POST', 'URL', headers={})

# with requests.get('https://wwww.baidu.com') as response:
#     print(response.status_code)

#   正则表达式

#  \ 将下一个字符标记为特殊字符， 例如\n匹配换行符， \\匹配 \
#  ^ 匹配输入字符串的开始位置
#  $ 匹配输入字符串的结束位置
#  * 匹配前面的子表达式零次活多次 ，*等价于{0,}
#  + 匹配前面的子表达式一次或者多次，+等价于{1,}
#  ? 匹配前面的子表达式零次或者一次，？等价于{0,1}
#  {n} n是一个非负整数，匹配确定的n次
#  {n,}n是一个非负整数，至少匹配n次
#  {n,m}n,m，均为非负整数，其中n<m，最少匹配n次，最多匹配m次
#  ？当该字符紧跟在任何一个其他重复修饰符(*,+,?,{n},{n,},{n,m})后面是，匹配的是非贪婪的，非贪婪模式尽可能少的匹配所搜索的字符串
#  . 匹配除 \n, \r外的任意单个字符，若要匹配 \n,\r请使用 .|\n|\r
#  \b 匹配一个单词的边界
#  \B 匹配非单词边界
#  \d 匹配一个数字字符，等价于[0-9]
#  \D 匹配一个非数字字符，等价于[^0-9]
#  [a-z] 匹配从a-z的返回内任意小写字符
#  [^a-z]匹配除从a-z的返回的任意字符
#  \f匹配一个换页符
#  \n匹配一个换行符
#  \r匹配一个回车键
#  \s匹配任何空白字符，包括空格，制表符，换页符等，等价于[\f\r\n\t\v]
#  \S 匹配任何非空白字符
#  \t  匹配制表符
#  \v匹配一个垂直制表符
#  \w 匹配包括下划线的任何单词字符，等价于[a-zA-Z0-9_]
#  \W 匹配任何非单词字符，等价于[^A-Za-z0-9_]

# bid=XahgAuOFM5k; douban-fav-remind=1; __gads=ID=a0f3d15f787e6989:T=1584428170:S=ALNI_Mb9uGcX1In51-F-wEpvH08_7NbXwA; __utmc=30149280; __utmz=30149280.1584428173.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.1568182175.1584428173.1586856761.1592295402.3; __utma=223695111.2082845409.1592295402.1592295402.1592295402.1; __utmc=223695111; __utmz=223695111.1592295402.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0; __yadk_uid=0sK9RiWMlB8NbzG8cOE1FvoIkKwdvHSc; _pk_id.100001.4cf6=3f4cfc31eeedc652.1592295402.1.1592296805.1592295402.