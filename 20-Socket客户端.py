# -*- coding: utf-8 -*-
"""
@Time ：2023-04-05 12:55
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import socket

# 创建socket对象
socket_client = socket.socket()
# 链接服务端
socket_client.connect(("localhost", 8080))

while True:
    # 发送消息
    msg = input("请输入要发送的消息：")
    if msg == "exit" or msg == "quit":
        break
    socket_client.send(msg.encode("UTF-8"))
    # 接收的回复消息
    data = socket_client.recv(1024).decode("UTF-8")
    print(f"接收到的消息；{data}")
socket_client.close()
