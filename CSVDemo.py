'''
@Author: Yang
@Date: 2020-06-22 14:07:16
@LastEditors: Yang
@LastEditTime: 2020-06-22 14:21:18
@FilePath: /python学习/CSVDemo.py
@Description: 头部
'''
import csv
import pandas

# with open('zz.csv', mode='w') as csv_file:
#     fileName = ['你是谁', '你几岁', '你多高']
#     writer = csv.DictWriter(csv_file, fileName)
#     writer.writeheader()
#     writer.writerow({'你是谁': 'shabi', '你几岁': '16岁', '你多高': '189'})
#     writer.writerow({'你是谁': 'shabi', '你几岁': '16岁', '你多高': '189'})
#     writer.writerow({'你是谁': 'shabi', '你几岁': '16岁', '你多高': '189'})

zz=pandas.read_csv('zz.csv')
print(zz)