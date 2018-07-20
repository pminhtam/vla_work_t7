import pyodbc
# from accounts.models import User

con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = 'DESKTOP-6O0KO5B\SQLEXPRESS', database ='sanpham')
cursor = con.cursor()

def listIdSp():
    query = "select id from danhsach"
    try:
        cursor.execute(query)
    except Exception:
        return False
    data = []
    for row in cursor.fetchall():
        data.append(int(row.id))
    return data
def codeAnalysis():
    listId = listIdSp()
    data = []
    for i in listId:
        query = "select COUNT(*) as code_count from dinhdanh where id_sp =" + str(i)
        try:
            cursor.execute(query)
        except Exception:
            return False
        for row in cursor.fetchall():
            data.append(int(row.code_count))
    return data
def getDataDanhSach():              # lấy thông tin về các sản phẩm đang tồn tại
    query = "select * from danhsach"
    try:
        cursor.execute(query)
    except Exception:
        return False
    data = []
    for row in cursor.fetchall():
        data.append(row)
    return data
# from ..api.utils import getDataDanhSach
# data = getDataDanhSach()

# for i in data:
#     print('\"' + i[1] + '\"')
def history():
    query = "select CAST(ngay_sinh as DATE),DATEPART(hour,ngay_sinh) as gio,sum(num) as sum_day from lichsu " \
            "group by CAST(ngay_sinh as date) ,DATEPART(hour,ngay_sinh) " \
            "order by CAST(ngay_sinh as date),DATEPART(hour,ngay_sinh)"
    try:
        cursor.execute(query)
    except Exception:
        return False
    data = []
    for row in cursor.fetchall():
        data.append(row)
    return data
# print(history())