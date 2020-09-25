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
            self.send_user()
            data = self.c.recv(1024)
            if data.decode() == "OK":
                print("注册成功")
                print("""
                *************************************
                1 直接登录
                2 返回首页
                *************************************
                """)
                msg = input("请输入选项:")
                if msg == "1":
                    self.search()
                elif msg == "2":
                    return
            elif data.decode() == "Error":
                print("用户名已存在!")
                return

    def send_user(self):
        name = input("Name:")
        passwd = input("Passwd:")
        self.c.send(name.encode() + b" " + passwd.encode())

    def log_in(self):
        data = self.c.recv(1024)
        while data.decode() == "OK":
            self.send_user()
            data = self.c.recv(1024)
            if data.decode() == "OK":
                print("登录成功")
                print("""
                *************************************
                1 查询单词
                2 产看历史记录
                *************************************
                """)
                msg = input("请输入选项:")
                if msg == "1":
                    self.search()
                elif msg == "2":
                    return
            elif data.decode() == "Error":
                print("用户名或密码不正确!")
                return

    def search(self):
        self.c.send(b"L")
        data = self.c.recv(1024)
        while True:
            msg = input("请输入要查询的单词:")
            self.c.send(msg.encode())
            data = self.c.recv(1024).decode()
            if data == "Error":
                print("没有这个单词!")
            else:
                print(data)




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
    #   注册功能
    if msg == "1":
        c.send(b"R " + msg.encode())
        Request(c).register()
    elif msg == "2":
        c.send(b"I " + msg.encode())
        Request(c).log_in()

