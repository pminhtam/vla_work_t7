from django.shortcuts import render
from django.http import HttpResponse
from . import utils
import os.path
# Create your views here.




"""
from pymongo import MongoClient
from bson import json_util
import json
from datetime import datetime
import redis


def findByKeyAPI(request):
    key = ""
    if request.method == "GET":
        key = request.GET.get('key')
    if request.method == "POST":
        key = request.POST.get('key')
    # print(key)
    client = MongoClient()
    db = client.thunghiem
    cursor = db.danhsach.find({"id": key})
    a = []
    for i in cursor:
        a.append(json.dumps(i, default=json_util.default))
    data = json.dumps(a)
    return HttpResponse(data, content_type='application/json')
def findByKeyWeb(request):
    key=""
    label="id"
    time_find =0
    # if request.method == "GET":
    #     key = request.GET.get('key')
    if request.method == "POST":
        label = request.POST.get('label')
        key = request.POST.get('key')
    # print(label)
    # print(key)
    if key!="":
        # start = datetime.now().timestamp()
        # client = MongoClient()
        # db = client.sp
        # cursor = db.ds.find({label : key}).limit(20)
        # end = datetime.now().timestamp()
        # time_find = end - start
        # data = []
        # # print(time_find)
        # for i in cursor:
        #     print(i)
        #     data.append(i)
        # return render(request,"pages/index.html",{"data" : data,'time':time_find})

###############################################Redis
        ##############################
        ######################
        start = datetime.now().timestamp()
        client = MongoClient()
        db = client.sp
        #r = redis.Redis(host="127.0.0.1", port=6379, password='')
        data = None
        status = ""
        if(label=="id"):
            data = None
            #data = r.get(key)
        if data != None:  # tim thay trong redis
            data = data.decode('utf-8')
            data = data.replace("'", "\"")
            data = json.loads(data)
            status = "Tìm thấy trong cache redis"
        elif data == None:  # khong tim thay
            data = []
            status = "Không có trong cache"
            print("khong tim thay trong redis")
            # count = db.ds.find({label: key}).count()
            # cur = []
            cur = db.ds.find({label: key}).limit(20)
            count = 0
            # count = cur.count()
            for i in cur:
                # print(i)
                i['_id'] = ''
                data.append(i)
            # r.set(key, json.dumps(data))
        end = datetime.now().timestamp()
        time_find = end - start
        return render(request, "pages/index.html", {"data": data, 'time': time_find,'status':status,'count':count})
    return render(request,"pages/find.html")


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def phantrang(request):
    start = datetime.now().timestamp()
    client = MongoClient()
    db = client.sp
    cursor = db.ds.find({"ten" : "Máy tính"})
    count = cursor.count()
    end = datetime.now().timestamp()
    time_find = end - start
    data_list = []
    # print(time_find)
    for i in cursor:
        # print(i)
        data_list.append(i)
    paginator = Paginator(data_list, 5)
    pageNumber = request.GET.get('page')
    try:
        data = paginator.page(pageNumber)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request,"pages/result.html",{"data" : data,'time':time_find,'count':count})
"""


def makeNum(request):
    if request.method == "POST":
        m = int(request.POST.get('m'))
        a = int(request.POST.get('a'))
        createdNumber = 0
        if os.path.isfile("daSinh.txt"):        # kiểm tra có tồn tại file ko
            f = open("daSinh.txt",'r')
            readFileResult = f.readline()                   # kiểm tra có đọc đc gì ko
            if readFileResult:
                createdNumber = int(readFileResult)                  # chuyển sang số
            f.close()
        # bias = 0
        li = utils.lcg(a, m, createdNumber)
        f = open("daSinh.txt",'w')              # lưu lại số lượng đã sinh
        f.writelines(str(createdNumber+m))
        f.close()
        utils.writeData(li, "data.csv")
        return render(request,'pages/makeNumResult.html',{"data":li})
    return render(request,'pages/makeNum.html')

def insertData(request):
    if request.user.is_staff==False:
        return render(request,'pages/error.html',{'data':'Bạn phải đăng nhập để thêm dữ liệu'})
    if request.method == "POST":
        id = int(request.POST.get('id'))
        ten = request.POST.get('ten')
        gia = request.POST.get('gia')
        result = utils.insert(id, ten, gia)
        if result==False:
            return render(request, 'pages/error.html', {'data': 'Thêm dữ liệu không thành công'})
            # return HttpResponse({'Thêm dữ liệu không thành công'})
        return render(request, 'pages/insertDataResult.html',{'id':id,'ten':ten,'gia':gia})
    return render(request,'pages/insertData.html')
def findData(request):
    key = ""
    label = "id"
    if request.method == "POST":
        label = request.POST.get('label')
        key = request.POST.get('key')
    if key != "":
        data = utils.find(label, key)
        return render(request, "pages/findResult.html", {"data": data})
    return render(request, "pages/find.html")

"""
API
"""
#######################
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def api_makeNum(request):
    if request.method == "POST":
        m = int(request.POST.get('m'))
        a = int(request.POST.get('a'))
        createdNumber = 0
        if os.path.isfile("daSinh.txt"):        # kiểm tra có tồn tại file ko
            f = open("daSinh.txt",'r')
            readFileResult = f.readline()                   # kiểm tra có đọc đc gì ko
            if readFileResult:
                createdNumber = int(readFileResult)                  # chuyển sang số
            f.close()
        # bias = 0
        listNum = utils.lcg(a, m, createdNumber)
        f = open("daSinh.txt",'w')              # lưu lại số lượng đã sinh
        f.writelines(str(createdNumber+m))
        f.close()
        utils.writeData(listNum, "data.csv")
        data = json.dumps({"listNum":listNum})
        return HttpResponse(data,content_type="application/json")
    return HttpResponse({'Không có dữ liệu'})
@csrf_exempt
def api_insertData(request):
    if request.method == "POST":
        id = int(request.POST.get('id'))
        ten = request.POST.get('ten')
        gia = request.POST.get('gia')
        result = utils.insert(id, ten, gia)
        if result==False:
            return HttpResponse({'Thêm dữ liệu không thành công'})
        data = json.dumps({'id':id,'ten':ten,'gia':gia})
        return HttpResponse(data,content_type="application/json")
    return HttpResponse({'Không có dữ liệu'})
@csrf_exempt
def api_findData(request):
    key = ""
    label = "id"
    if request.method == "POST":
        label = request.POST.get('label')
        key = request.POST.get('key')
        print(label)
        print(key)
    if key != "" and key!=None:
        data = utils.find(label, key)  # trả lại dưới dạng đổi tượng sql
        # cần chuyển về dạng danh sách
        data_re = []
        for i in data:
            element = {"id":str(i.id),"ten":i.ten,"gia":i.gia}
            data_re.append(element)
        data_re = json.dumps(data_re)       # chuyển dữ liệu về dạng json
        return HttpResponse(data_re,content_type="application/json")
    return HttpResponse({'Không có dữ liệu'})
