# -*- coding: utf-8 -*-
"""
@Time ：2023-04-05 12:12
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import threading
import time


def sing():
    while True:
        print("唱歌")
        time.sleep(1)


def dance():
    while True:
        print("跳舞")
        time.sleep(1)


def action(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # =============== 一个线程
    # sing()
    # dance()

    # =============== 多个线程
    # group：暂时无用，未来功能的预留参数
    # target：执行的目标任务名
    # args：以元组的方式给执行任务传参
    # kwargs：以字典的方式给执行任务传参
    # name：线程名，一般不用设置
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)
    thread_action = threading.Thread(target=action, kwargs={"msg": "=唱歌并跳舞="})

    thread_sing.start()
    thread_dance.start()
    thread_action.start()
