'''
@Author: Yang
@Date: 2019-11-06 16:09:32
@LastEditors: Yang
@LastEditTime: 2019-11-07 09:45:52
@FilePath: /Python/regular.py
@Description: 
'''

import re


def main():
    userName = input('请输入您的用户名：')

    # m1 = re.match(r'^/w{6,20}$', userName)

    # if not m1:
    #     print('请输入有效的用户名')

    # qq = input('请输入您的qq账号：')
    # m2 = re.match(r'^[1-9]/d{4,11}&', qq)
    # if not m2:
    #     print('请输入有效的QQ号.')
    # if m1 and m2:
    #     print('你输入的信息是有效的!')
    m1 = re.match(r'(?>=abc)\d\s')
    if m1:
        print(m1)


if __name__ == "__main__":
    main()

"""
 . 用来匹配任何单个字符，换行符除外
 [] 匹配字符集合
 \d 数字字符，等价于[0-9]
 \D 非数字字符，等价于[^0-9]
 \w 字母数字下划线，等价于[a-z0-9A-Z_]
 \W 非数字字母下划线，等价于[^a-z0-9A-Z_]
 \s 空白字符，换行，换页，制表符等，等价于[\f\r\n\v\t]
 \S 非空白字符
 

"""
