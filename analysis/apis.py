from django.shortcuts import render
from django.http import HttpResponse
from . import utils
import json
# from app.utils import getDataDanhSach
# Create your views here.

def api_codeAnalysis(request):
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
    data = json.dumps({'code': 1, 'status': 'Thành công', 'ten': ten,'num':count})
    return HttpResponse(data, content_type="application/json")
def api_price(request):
    danhsach = utils.getDataDanhSach()
    ten = []
    gia = []
    for i in danhsach:
        ten.append(i[1])
        gia.append(int(i[2]))
    data = json.dumps({'code': 1, 'status': 'Thành công', 'ten': ten,'num':gia})
    return HttpResponse(data, content_type="application/json")
def api_history(request):
    data = utils.history()
    ngay = []
    soluong = []
    for i in data:
        ngay.append(i[0]+"  "+str(i[1]) + "h")
        soluong.append(int(i[2]))
    data = json.dumps({'code': 1, 'status': 'Thành công', 'ten': ngay,'num':soluong})
    return HttpResponse(data, content_type="application/json")