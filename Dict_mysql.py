"""
电子词典数据库程序
"""
import pymysql
import sys
import re

class Dict_mysql:
    def __init__(self, c):
        self.c = c
        self.db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='123456',
                     database='dict',
                     charset='utf8')
        self.cur = self.db.cursor()
    def add(self,name,passwd):
        cheack = "SELECT * FROM user WHERE name='%s';" % name
        if self.cur.execute(cheack):
            return False
        else:
            sql = "INSERT INTO user (name,passwd) VALUES ('%s','%s');" % (name,passwd)
            self.cur.execute(sql)
            self.db.commit()

            return True
    def varify(self,name,passwd):
        sql = "SELECT * FROM user WHERE name='%s' and passwd='%s'" % (name,passwd)
        if self.cur.execute(sql):
            return True
        else:
            return False
    def look_for(self,word):
        sql = "SELECT * FROM words WHERE word='%s'" % word
        self.cur.execute(sql)
        data = self.cur.fetchone()
        if data:
            return data[2]

        else:
            return False
    def update(self):
        fd = open("dict.txt",'r')
        for i in range(3):
            data = fd.readline()
            data = re.split(r" {3}",data)
            print(data)
            # sql = "SELECT * FROM words WHERE word='%s' and comment='%s'" % (data[1], data[2])
            # self.cur.execute(sql)
            # if self.cur.fetchone():
            #     print(data[1],"已存在")
            #     continue
            # else:
            #     sql = "INSERT INTO words (word,comment) VALUES ('%s','%s')" % (data[1],data[2])
            #     self.cur.execute(sql)

if __name__ == '__main__':
    Dict_mysql(1).update()


