
# -*- coding:utf-8 -*-             # 声明使用编码
import pymysql
import random
class mysql(object):
    def mysql(abc): #定义一个函数，abc是默认的参数
        connection = pymysql.connect(host='172.17.210.115', user='retail_fas', password='retail_fas', db='retail_fas',port=8066, charset='utf8')
        cursor = connection.cursor()# 使用cursor()方法获取操作游标
        sql=abc
        cursor.execute(sql)#通过execute方法执行sql
        #result = cursor.fetchone()  # 查询数据库单条数据
        result = cursor.fetchall() #查询数据库多条数据
        connection.close()  # 关闭数据库
        return result

    sql1 = mysql(r"select * from store_group") #数据库查询语句，前面加r的意思是格式不变
    sql2 = mysql(r"select order_no from order_main limit 1")  # 数据库查询语句，前面加r的意思是格式不变
