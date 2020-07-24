'''
@Author: Yang
@Date: 2020-06-22 15:11:58
@LastEditors: Yang
@LastEditTime: 2020-07-01 16:28:51
@FilePath: /python学习/mysql.py
@Description: 头部注释
'''

import pymysql

db = pymysql.connect(host='localhost', user='root',
                     db='yang', passwd='12345678',)
cursor = db.cursor()
sql = """create table if not exists person (id int not null auto_increment, name text not null,age int,sex int,height int,primary key (id))default charset=utf8"""
cursor.execute(sql)
b = 'xiaogou'
c = 4
d = 0
e = 35
insertSql = "insert into person(name, age, sex, height) values('%s',%s,%s,%s)" % (
    b, c, d, e)
res = cursor.execute(insertSql)
print(res)
# 最后我们关闭这个数据库的连接
cursor.connection.commit()
db.close()
