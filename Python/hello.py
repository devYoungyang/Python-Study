'''
@Author: Yang
@Date: 2019-10-24 13:24:45
@LastEditors: Yang
@LastEditTime: 2019-11-12 14:48:53
@FilePath: /Python/hello.py
@Description:
'''

from tkinter import *
import tkinter.messagebox
import turtle
import urllib
import doctest
import zlib
import datetime
import random
import math
import re
import glob
import tkinter
import os.path
import os
import pprint
import pickle
from collections import deque
import sys
import stat
'''
from sys import path
import sys
import keyword
print("Hello,World !")
print(keyword.kwlist)
x = "runoob"
sys.stdout.write(x + '\n')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
print('path', path)
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

a, b = 10, 20
if a == b:
    print('a等于b')
else:
    print('a不等于b')
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2)*5
    print("对应人类年龄: ", human)

# 退出提示
input("点击 enter 键退出")



languages = ('C', 'C++', 'Python', 'Java')
for lan in languages:
    print(lan)
for i in range(1, 100, 5):
    print(i, end=',')


list = [1, 2, 3, 4, 5, 6]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
'''

"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for i in myiter:
    print(i)
"""
# 斐波那契数列
"""
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1


f = fibonacci(10)

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
"""
# 函数
"""
def methodName(a):
    a = a**a
    return a

print(methodName(5))
"""


"""
def changeInt(a):
    a = 10


b = 5
changeInt(b)
print(b)
"""

"""
def changeme(mylist):
    mylist.append([5, 6, 7, 8])
    print("函数内取值", mylist)


list = [1, 2, 3, 4]
changeme(list)
print("函数外取值", list)
"""
"""
queue = deque(["Eric", "John", "Michael"])

print(queue.popleft())
# 列表推导式
vec = [1, 2, 3, 4]
vec2 = [1, 2, 3]
aa = [2*x for x in vec]
print(aa)
bb = [[x, x**2] for x in vec]
print(bb)
# 使用if子句
cc = [2*x for x in vec if x > 3]
print(cc)

dd = [x*y for x in vec for y in vec2]
print(dd)

ee = [str(round(355/113, i)) for i in range(1, 20)]
print(ee)
"""
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
"""
"""
if __name__ == "__main__":
    print('程序自身在运行')
else:
    print('我是被引入进来的')

# print(dir(sys))

print(dir())

str = input('请您输入：')
print('您输入的是：', str)
"""

"""
f = open("./foo.txt", "rb+")
# f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# print(f.readline())
# print(f.seek(5, 0))
# print(f.read(1))
f.close()

with open("./second.txt", "r+") as s:
    # s.write('HAHAHAHA')
    print(s.read())
f.closed
"""
"""
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', "wb")
pickle.dump(data1, output)
pickle.dump(selfref_list, output)
output.closed
"""

"""
pkl_file = open('data.pkl', 'rb')
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
data3 = pickle.load(pkl_file)
pprint.pprint(data3)
pkl_file.close()
"""
"""
ls = []
def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            if True == os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.')+1:].upper() == 'PY':
                ls.append(pathTmp)
    except PermissionError:
        pass


while True:
    path = input('请输入路径:').strip()
    if os.path.isdir(path) == True:
        break

getAppointFile(path, ls)
# print(len(ls))
print(ls)
print(len(ls))
"""
# print(os.access("./", os.R_OK)

"""
print('当前工作目录:', os.getcwd())
os.chdir('./tamp')
print('当前工作目录:', os.getcwd())

os.chmod('./tamp', stat.S_IXUSR)  # 设置文件可以被拥有者执行
"""
# print(os.openpty())
# os.rename("tamp", "tamps")  # 重命名文件或目录，

"""

class Person:
    name = "tOM"
    age = ""

    # def __init__(self):    #类的构造方法
    # self.name = name
    # self.age = age

    def eat(self):  # 类方法的第一个参数必须为self
        print('吃饭了～')

    def run(self):
        print('运动了～')


p = Person()  # 创建类实例   即对象
p.eat()
p.name = "HAHA"
print(p.name)


class Student(Person):  # 继承
    def study(self):
        print('学习英语～')


s = Student()
s.study()
"""


a = "1"
b = "2"

"""
def changedA():
    global a
    a = "1111"


changedA()
print(a)
"""


def main():
    os.system('./shell.sh ' + a+' '+b)  # 调用shell脚本并传入参数


"""

print(glob.glob('*.py'))
print(sys.argv)


c = random.choice(['A', 'B', 'C'])
print(c)
d = random.random()
print(d)
e = random.randrange(11, 20)
print(e)
"""

"""
print(datetime.date.today())


def average(values):
    return sum(values) / len(values)


print(average([10, 20, 30]))
doctest.testmod()
"""

"""

top = tkinter.Tk()


def exec():
    print('Hello world')


B = tkinter.Button(top, text="点我", command=exec)
B.pack()
top.mainloop()
"""
"""

def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():

        os.system('./shell.sh')
        # nonlocal flag
        # flag = not flag
        # color, msg = ('red', 'Hello, world!')\
        #     if flag else ('blue', 'Goodbye, world!')
        # label.config(text=msg, fg=color)

        # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('640x860')
    # 设置窗口标题
    top.title('Package')
    label = tkinter.Label(top, text="Model")
    label.pack(side="right")
    # 创建标签对象并添加到顶层窗口
    entry = tkinter.Entry(top, bd=4)
    entry.pack()

    button = tkinter.Radiobutton(top)
    button.pack()
    label = tkinter.Label(top, text='Hello, world!',
                          font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
"""


class App:

    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建第一个容器
        fm1 = Frame(self.master,)
        # 该容器放在左边排列
        fm1.pack(pady=30)
        # 向fm1中添加3个按钮
        # 设置按钮从顶部开始排列，且按钮只能在垂直（X）方向填充
        Label(fm1, text='请输入设备的model:',).pack(side=LEFT,)
        e = Entry(fm1,)
        e.pack(side=LEFT)
        var = tkinter.StringVar()
        # 创建第二个容器
        fm2 = Frame(self.master)
        # 该容器放在左边排列，就会挨着fm1
        fm2.pack(side=TOP, pady=10, expand=YES)
        # 向fm2中添加3个按钮
        # 设置按钮从右边开始排列
        Label(fm2, text="请选择设备类型：").pack()
        Radiobutton(fm2, text='bright               ', variable=var,
                    value='1', ).pack(side=TOP)
        Radiobutton(fm2, text='brightCCT        ', variable=var, value='2',
                    ).pack(side=TOP)
        Radiobutton(fm2, text='brightCctColor', variable=var, value='3',
                    ).pack(side=TOP,)
        # 创建第三个容器
        fm3 = Frame(self.master)
        # 该容器放在右边排列，就会挨着fm1
        fm3.pack(side=BOTTOM, pady=20, fill=Y, expand=NO)
        # 向fm3中添加3个按钮
        # 设置按钮从底部开始排列，且按钮只能在垂直（Y）方向填充

        def print_selection():
            # print(e.get(), var.get())
            a = e.get()
            b = var.get()
            os.system('./shell.sh ' + a+' '+b)

        b3 = Button(fm3, text='执行', width="10",  command=print_selection)
        b3.pack(side=LEFT, fill=Y, expand=NO)


root = Tk()
root.title("Package")
root.geometry('840x400')


display = App(root)
root.mainloop()
