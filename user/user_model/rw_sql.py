#coding:utf-8
from edianzu.setMysql import cursor,db

def write_sql(sql):
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        return False

def read_sql(sql):
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    return data