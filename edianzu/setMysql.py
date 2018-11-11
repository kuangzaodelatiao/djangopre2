import pymysql
db = pymysql.connect('192.168.8.112','root','123456','edianzu')

cursor = db.cursor()
# sql = 'select * from goods'
# data = cursor.execute(sql)
# print(data)
