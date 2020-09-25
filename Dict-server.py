"""
电子词典服务器
"""

import socket
import sys,os
from Dict_mysql import *
import signal

IP = "127.0.0.1"
PORT = 8080
ADDR = (IP,PORT)

s = socket.socket()
s.bind(ADDR)
s.listen(5)
signal.signal(signal.SIGCLD, signal.SIG_IGN)
print("Waiting for connect...................")

class Handle:
    def __init__(self,c):
        self.c = c

    def add_user(self):
        self.c.send(b"OK")

        data = self.c.recv(1024)
        # print(data)
        name = data.decode().split(" ")[0]
        passwd = data.decode().split(" ")[1]
        # print(name)
        # print(passwd)
        if Dict_mysql(c).add(name,passwd):
            self.c.send(b"OK")
        else:
            self.c.send(b"Error")




while True:


    try:
        c,addr = s.accept()

    except KeyboardInterrupt:
        sys.exit("服务器关闭")
    except Exception as e:
        print("Error:",e)
        continue
    pid = os.fork()
    if pid == 0:
        s.close()
        print("Client is:", c.getpeername)
        while True:
            data = c.recv(1024).decode()
            if not data:
                print("客户端已退出")
                os._exit(0)
            print(data)
            if data[0] == "R":
                Handle(c).add_user()



    else:
        c.close()
