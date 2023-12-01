# -*- coding: utf-8 -*-
"""
@Time ：2023-04-05 12:29
@Auth ：谁书-ss
@IDE  ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import socket

# 创建socket对象
socket_server = socket.socket()
# 绑定ip port
socket_server.bind(("localhost", 8080))
# 监听端口链接数量
socket_server.listen(1)
# 等待客户端链接：accept()是阻塞的
conn, address = socket_server.accept()
print(f"接收客户端链接信息：conn:{conn}, address:{address}")

while True:
    # 接收客户端信息
    # recv 接收参数是缓冲区大小，一般是 1024。返回值是一个字节数组bytes对象，可以通过decode方法编码，将字节数组转换为字符串
    data = conn.recv(1024).decode("UTF-8")
    print(f"接收到的消息；{data}")
    # 发送回复消息
    # encode将字符串编码为字节数组
    msg = input("请输入要回复的消息：")
    if msg == "exit" or msg == "quit":
        break
    conn.send(msg.encode("UTF-8"))
# 关闭链接
conn.close()
socket_server.close()
