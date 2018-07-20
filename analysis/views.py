from django.shortcuts import render
from django.http import HttpResponse
from . import utils
# from api.utils import getDataDanhSach
# Create your views here.

def codeAnalysis(request):
    count = utils.codeAnalysis()
    print(count)
    danhsach = utils.getDataDanhSach()
    # print(danhsach)
    ten = []
    for i in danhsach:
        ten.append(i[1])
        # print(str(i[1]))
    # print(ten)
    # print(count)
    return render(request,'codeAnalysis.html',{'title':'Thống kê số mã đã tạo','ten':ten,'num':count})

def price(request):
    danhsach = utils.getDataDanhSach()
    ten = []
    gia = []
    for i in danhsach:
        ten.append(i[1])
        gia.append(int(i[2]))
    return render(request,'codeAnalysis.html',{'title':'Giá sản phẩm','ten':ten,'num':gia})

def history(request):
    data = utils.history()
    ngay = []
    soluong = []
    for i in data:
        ngay.append(i[0]+"  "+str(i[1]) + "h")
        soluong.append(int(i[2]))
    return render(request,'codeAnalysis.html',{'title':'Lịch sử tạo mã','ten':ngay,'num':soluong})
