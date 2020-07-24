'''
@Author: Yang
@Date: 2019-10-31 17:15:32
@LastEditors: Yang
@LastEditTime: 2019-10-31 17:27:00
@FilePath: /Python/demo.py
@Description: 
'''

from tkinter import *
import tkinter.messagebox

import tkinter
import os
import sys
import stat


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
        Radiobutton(fm2, text='bright  ', variable=var,
                    value='1', ).pack(side=LEFT)
        Radiobutton(fm2, text='brightCCT  ', variable=var, value='2',
                    ).pack(side=LEFT)
        Radiobutton(fm2, text='brightCctColor  ', variable=var, value='3',
                    ).pack(side=LEFT)
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

        b3 = Button(fm3, text='执行', width="10",  command=print_selection)
        b3.pack(side=LEFT, fill=Y, expand=NO)


root = Tk()
root.title("Package")
root.geometry('840x400')


display = App(root)
root.mainloop()
