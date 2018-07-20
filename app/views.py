from django.shortcuts import render
from . import utils
import os.path
# Create your views here.
from .makeCode import makeCode
def makeNum(request):
    if request.user.is_staff==False:
        return render(request,'pages/error.html',{'data':'Bạn phải đăng nhập Hoặc bạn không có quyền sinh số'})
    if request.method == "POST":
        id_sp = int(request.POST.get('id'))
        m = int(request.POST.get('m'))              # số lượng sinh
        a = int(request.POST.get('a'))
        num_sum =utils.getCreatedNum()
        li = utils.lcg(a, m, num_sum)
        result_code_dict = makeCode(li,id_sp)
        # print(li[0:2])
        checksum_list = result_code_dict['checksum_list']
        code_list = result_code_dict['code_list']
        year = result_code_dict['year']
        group2_list = result_code_dict['group2_list']
        group3 = result_code_dict['group3']
        list_zip = zip(group2_list,checksum_list,code_list)
        result = utils.insertDataDinhDanh(id_sp,code_list,m,num_sum)
        print(result)
        if result == False:
            return render(request, 'pages/error.html', {'data': 'Thêm không thành công','code':li})

        ## tạo mã thành công
        return render(request,'pages/makeNumResult.html',{'list_zip':list_zip,
                                                         'year':year,'group3':group3,
                                                          'range':range(10)})
    data_ds = utils.getDataDanhSach()
    if data_ds == False:
        return render(request, 'pages/error.html', {'data': 'Không có dữ liệu'})
    return render(request,'pages/makeNum.html',{'data':data_ds})
def listMa(request):
    data = []
    if request.method == "POST":
        begin = request.POST.get('begin')
        end = request.POST.get('end')
        data = utils.listMa(begin,end)
    return render(request,'pages/listMa.html',{'data':data})

def insertData(request):
    if request.user.is_staff==False:
        return render(request,'pages/error.html',{'data':'Bạn phải đăng nhập Hoặc bạn không có quyền thêm dữ liệu'})
    if request.method == "POST":
        # id = int(request.POST.get('id'))
        ten = request.POST.get('ten')
        gia = request.POST.get('gia')
        result = utils.insert(ten, gia)
        if result==False:
            return render(request, 'pages/error.html', {'data': 'Thêm dữ liệu không thành công'})
        return render(request, 'pages/insertDataResult.html',{'ten':ten,'gia':gia})
    return render(request,'pages/insertData.html')  #màn hình chèn dữ liệu

def findData(request):
    key = ""
    label = "id"
    if request.method == "POST":
        label = request.POST.get('label')
        key = request.POST.get('key')
    if key != "":
        data = utils.find(label, key)
        if data == False or len(data)<1:
            return render(request, 'pages/error.html', {'data': 'Không thấy dữ liệu'})
        return render(request, "pages/findResult.html", {"data": data})
    return render(request, "pages/find.html")

def findDataMa(request):
    if request.method == "POST":
        ma_dd = request.POST.get('ma_dd')
        id = utils.findMa(ma_dd)                # tìm id_sp theo mã định danh sản phẩm
        if id == False:                         # không tìm thấy
            return render(request, 'pages/error.html', {'data': 'Không thấy sản phẩm'})
        # print("DATA MA "+ str(id))
        data = utils.find("id",str(id))         # tìm sản phẩm theo id vừa nhận được
        if data == False or len(data)<1:
            return render(request, 'pages/error.html', {'data': 'Không thấy dữ liệu'})
        return render(request, "pages/findResult.html", {"data": data})
    return render(request, "pages/findMa.html")

