#!/usr/bin/env python
#-*- coding:utf8 -*-
import pymysql
conn = pymysql.connect(database='myweb',user='root',password='ROOT123',host='localhost',port=3306)

cursor = conn.cursor()

sql = "insert into mysite_goods(goods_name,goods_number,goods_price) values(%s,%s,%s);" 

with open('goods_list.txt','r') as f:
	for lines in f:
		li = lines.split()
		for goods in li:
			good = tuple(str(i) for i in goods.split(','))
			#print(good)
			print(good)
			print(sql %good)
			#cursor.execute(sql %good)

cursor.execute('insert into mysite_goods(goods_name,goods_number,goods_price) values("自动笔芯",36,2.1);')
