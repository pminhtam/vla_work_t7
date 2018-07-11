from datetime import datetime
import random
import pyodbc

# import csv
def lcg(a,m,bias):      # thuật toán tạo số ngẫu nhiên
    x = int(datetime.now().timestamp())%20
    c_li = [1, 3,5]

    c = random.choice(c_li)
    li = []
    for i in range(m):
        b = a*x+c
        (_ , x) = divmod(b,m)
        li.append(x+bias)
    return li
def writeData(list,filename):
    myFile = open(filename, 'w')
    for i in list:
        myFile.write(str(i)+'\n')

con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = 'DESKTOP-6O0KO5B\SQLEXPRESS', database ='sanpham')
cursor = con.cursor()

def insert(id,ten,gia):
    query = "insert into danhsach values ('" + str(id) + "',N'" + ten + "','" + gia + "')"
    try:
        cursor.execute(query)
    except Exception:
        return False
    con.commit()
    return True
def find(label,key):
    query = "select * from danhsach where "+label+"=N'" + key + "'"
    try:
        cursor.execute(query)
    except Exception:
        return False
    data = []
    for row in cursor.fetchall():
        data.append(row)
    return data