'''
@Author: Yang
@Date: 2020-06-22 14:27:03
@LastEditors: Yang
@LastEditTime: 2020-06-22 14:29:18
@FilePath: /python学习/PandasDemo.py
@Description: 头部注释
'''
import pandas as pd

a=['张三','李四','王二']
b=['男','男','女']
c=['173','188','167']
df=pd.DataFrame({'姓名':a,'性别':b,'身高':c})
df.to_csv('aa.csv',index=False,sep=',')