import sqlite3
import random
# .db - malumot ombori 

# SQL - ma'lumot ombori tili 

# omborni bog'lanish uchun obyekt
con = sqlite3.connect("./main.db", check_same_thread=False)
# omborni boshqarish uchun obyekt
cur = con.cursor()


# sql = """CREATE TABLE students(
#     name TEXT,
#     age INTEGER,
#     point INTEGER);"""
    
# cur.execute(sql)
# names = ["mike","sara","dean","bob","marcus","alex","fabio","rafa","dani","miguel"]
# for i in range(10):
#     sql = f"""INSERT INTO students(name,age,point)
#         VALUES('{names[i]}',{random.randint(7,18)},{random.randint(1,5)});"""
#     try:
#         cur.execute(sql)
#     except sqlite3.DatabaseError as error:
#         print(error)
#     else:
#         con.commit() # omborga ma'lumotlarni kiritishni tasdiqlash
# else:
#     cur.close() # omborni boshqarishni to'xtatish
#     con.close() # bog'lanishni yopish


# sql = """SELECT * FROM students"""
# data = cur.execute(sql)
# for i in data.fetchall():
#     print(i)

# sql = """SELECT name,point FROM students"""
# data = cur.execute(sql)
# for i in data.fetchall():
#     print(i)

# data = cur.execute("SELECT name,point FROM students WHERE name='bob'")
# print(data.fetchone())

# data = cur.execute("SELECT name,point FROM students WHERE point >= 3 ")
# print(data.fetchall())

# data = cur.execute("SELECT name,point FROM students WHERE point = 3 ")
# print(data.fetchall())
# no data