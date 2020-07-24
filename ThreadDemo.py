'''
@Author: Yang
@Date: 2020-06-17 16:32:42
@LastEditors: Yang
@LastEditTime: 2020-07-07 14:08:43
@FilePath: /python学习/ThreadDemo.py
@Description: 头部注释
'''
import _thread
import random
import concurrent
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import time
import threading
from multiprocessing import Process
from multiprocessing import Pool

import multiprocessing
# class MyThread(threading.Thread):
#     def __init__(self, threadID, name, delay):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.delay = delay

#     def run(self):
#         print('开启线程:' + self.name)
#         moyu_time(self.name, self.delay, 10)
#         print('结束线程:' + self.name)


# def moyu_time(name, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("%s 开始摸鱼 %s" % (name, time.strftime(
#             '%Y-%m-%d %H:%M:%S', time.localtime())))
#         counter -= 1


# thread1 = MyThread(1, '小明', 1)
# thread2 = MyThread(2, '小红', 2)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print('推出主线程')

# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(20)
#     for i in range(1, 5):
#         pool.submit(moyu_time('摸鱼用户'+str(i), 2, 3))


# class CustomThread(threading.Thread):
#     def __init__(self, queue):
#         threading.Thread.__init__(self)
#         self.__queue = queue

#     def run(self):
#         while True:
#             q_method = self.__queue.get()
#             q_method()
#             self.__queue.task_done()


# def moyu():
#     print(" 开始摸鱼 %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


# def queue_pool():
#     queue = Queue(5)
#     for i in range(queue.maxsize):
#         t = CustomThread(queue)
#         t.setDaemon(True)
#         t.start()
#     for i in range(20):
#         queue.put(moyu)
#     queue.join()


# if __name__ == "__main__":
#     queue_pool()

def f(name):
    print('hello', name)


def x(x):
    time.sleep()
    return x*x


if __name__ == "__main__":
    # p = Process(target=f, args=('xiaoming',))
    # p.start()
    # p.join()

    # with Pool(5) as p:
    #     print(p.map(x, [1, 2, 3, 4, 5]))

    names = ['zhangsan', 'lisi', 'xiaohong', 'ersha', 'goudan']
    # 多进程
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # pool.map(f, names)
    # pool.close()
    # pool.join()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as exector:
        for name in names:
            exector.submit(f, name)
