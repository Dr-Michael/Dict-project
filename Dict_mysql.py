"""
电子词典数据库程序
"""
import pymysql

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
