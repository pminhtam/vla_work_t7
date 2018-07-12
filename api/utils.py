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

def insert(ten,gia):
    # query = "insert into danhsach values ('" + str(id) + "',N'" + ten + "','" + gia + "')"
    query = "insert into danhsach values (N'" + ten + "','" + gia + "')"

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
def findMa(ma_dd):
    query = "select * from dinhdanh where ma_dd='" + ma_dd + "'"
    try:
        cursor.execute(query)
    except Exception:
        return False
    data = []
    for row in cursor.fetchall():
        data.append(int(row.id_sp))
    if len(data)>0:
        return data[0]
    return False
########################
# Tạo token
import jwt
from accounts.models import User
def createToken(username,password):
    data = {
        'username': username,
        'password': password,
        'timestamp': datetime.now().timestamp()
    }
    # jwt = PyJWT()
    token = jwt.encode(data, "SECRET_KEY")
    return token
def getUsernameFromToken(token):
    try:
        data = jwt.decode(token,"SECRET_KEY")
    except Exception:
        return None,None,None
    username = data['username']
    password = data['password']
    time = data['timestamp']
    return  username,password,time
def checkUser(username,password):
    user = User.objects.get(username=username)
    if user:
        return user.check_password(password)
    return False
def verifyToken(token):                         # kiểm ta tài khoản mật khẩu
    username,password,time = getUsernameFromToken(token)
    if username == None:
        return False
    if time - datetime.now().timestamp() >100000:       # token quá hạn
        return False
    return checkUser(username,password)

def isAdminFromToken(token):                        # kiểm tra xem có phải là admin ko
    username,password,time = getUsernameFromToken(token)
    if username == None:
        return False
    if time - datetime.now().timestamp() >100000:       # token quá hạn
        return False
    if checkUser(username,password):
        return User.objects.get(username=username).is_staff
#tạo form đăng ký qua api
import re
class RegisterAPI:
    def __init__(self,username,email,pass1,pass2):
        self.username = username
        self.email = email
        self.pass1 = pass1
        self.pass2 = pass2
    def clean_password2(self):      # kiểm tra 2 mật khẩu có giống nhau ko
        if self.pass1 == self.pass2 and self.pass1:                # kiểm tra 2 mật khẩu có giống nhau không
            return True
        return False
    def clean_username(self):       # kiểm tra user có tồn tại ko
        if not re.search(r'^\w+$',self.username):
            return False            # tên không hợp lệ
        try:
            User.objects.get(self.username)
        except:
            return True             # user chưa tồn tại
        return False
    def save(self):
        if self.clean_password2() and self.clean_username():
            user = User.objects.create_user(username=self.username,email=self.email,password=self.pass1)
            user.save()
            return True
        return False

class EditAPI:
    def __init__(self,username,ten,diachi,SDT,gioitinh,chucvu):
        self.username = username
        self.ten = ten
        self.diachi = diachi
        self.SDT = SDT
        self.gioitinh = gioitinh
        self.chucvu = chucvu

    def save(self):
        try:
            user = User.objects.get(username=self.username)
        except:
            return False
        if self.ten !='':
            user.ten = self.ten
        if self.diachi !='':
            user.diachi = self.diachi
        if self.SDT !='':
            user.SDT = self.SDT
        if self.gioitinh !='':
            user.gioitinh = self.gioitinh
        if self.chucvu !='':
            user.chucvu = self.chucvu
        user.save()
        return True


####################
### Xác định mã định danh
def getCreatedNum():
    query = "select max(num_sum) as num_sum from lichsu"
    try:
        cursor.execute(query)
    except Exception:
        return 0
    data = []
    for row in cursor.fetchall():
        if row.num_sum == None:
            return 0
        data.append(int(row.num_sum))
    return data[0]
def insertDataDinhDanh(id_sp,li,m,num_sum):
    ###     m  số lượng vừa sinh
    ###     createdNumber : số lượng đã sinh
    for i in li:
        query = "insert into dinhdanh values ('" + str(id_sp) +"','" + str(i) + "')"
        try:
            cursor.execute(query)
        except Exception:
            return False
    time = datetime.now().strftime("%Y/%m/%d %H:%M")
    num_sum = num_sum+m
    query = "insert into lichsu(num,num_sum,ngay_sinh) values ('" + str(m) + "','" + str(num_sum) + "','" + str(time) + "')"
    try:
        cursor.execute(query)
    except Exception:
        return False

    con.commit()
    return True

def getDataDanhSach():
    query = "select * from danhsach"
    try:
        cursor.execute(query)
    except Exception:
        return False
    data = []
    for row in cursor.fetchall():
        data.append(row)
    return data