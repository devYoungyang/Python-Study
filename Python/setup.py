'''
@Author: Yang
@Date: 2019-10-29 10:38:48
@LastEditors: Yang
@LastEditTime: 2019-11-01 10:59:49
@FilePath: /Python/setup.py
@Description: 
'''
"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""


from setuptools import setup
APP = ['hello.py']
DATA_FILES = []
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
