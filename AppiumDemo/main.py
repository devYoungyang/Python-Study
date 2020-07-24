'''
@Author: Yang
@Date: 2020-06-23 13:54:16
@LastEditors: Yang
@LastEditTime: 2020-06-23 15:02:58
@FilePath: /python学习/AppiumDemo/main.py
@Description: 头部注释
'''

from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': '2ccde6c5',
    'platformVersion': '7.0.16',
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
