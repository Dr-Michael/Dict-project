"""
电子词典客户端
"""

import socket
import sys

IP = "127.0.0.1"
PORT = 8080
ADDR = (IP,PORT)

c = socket.socket()
c.connect(ADDR)

class Request:
    def __init__(self,c):
        self.c = c
    def register(self):
        data = self.c.recv(1024)
        while data.decode() == "OK":
            name = input("Name:")
            passwd = input("Passwd:")
            self.c.send(name.encode() + b" " + passwd.encode())
            data = self.c.recv(1024)
            if data.decode() == "OK":
                print("注册成功")
                return
            elif data.decode() == "Error":
                print("用户名已存在!")
                return





while True:
    print("""
    *************************
    1  注册
    2  登录
    """)
    try:
        msg = input("请输入选项:")
    except KeyboardInterrupt:
        sys.exit("客户端关闭")
    if msg == "1":
        c.send(b"R " + msg.encode())
        Request(c).register()
