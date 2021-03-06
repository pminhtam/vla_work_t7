#######################################################################
"""
API
"""
#######################################################################
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from . import utils
from .makeCode import makeCode

@csrf_exempt
def api_login(request):             # đăng nhập nếu thành công trả lại token
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if utils.checkUser(username,password):
            token = utils.createToken(username,password).decode('utf-8')
            data = json.dumps({'code': 1, 'status': 'Đăng nhập thành công','token':token})
            return HttpResponse(data,content_type="application/json")
    return HttpResponse(json.dumps({'code': 0, 'status': 'Không có dữ liệu'}),content_type="application/json")

@csrf_exempt
def api_register(request):             # đăng nhập nếu thành công trả lại token
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if utils.registerAPI(username,email,password1,password2).save():
            if utils.checkUser(username, password1):            # đăng ký thành công thì đăng nhập luôn
                token = utils.createToken(username, password1).decode('utf-8')
                data = json.dumps({'code': 1, 'status': 'Đăng ký thành công','token':token})    # trả lại token
                return HttpResponse(data,content_type="application/json")
    return HttpResponse(json.dumps({'code': 0, 'status': 'Không có dữ liệu'}),content_type="application/json")

from accounts.models import User
@csrf_exempt
def api_verifyToken(request):
    if request.method == "POST":
        token = request.POST.get('token')
        if utils.verifyToken(token):
            username, password, time = utils.getUsernameFromToken(token)
            user = User.objects.get(username=username)
            data = json.dumps({'code': 1, 'status': 'Đăng nhập thành công','username':username,'ten':user.ten,
                               'diachi':user.diachi,'SDT':user.SDT,'gioitinh':user.gioitinh,'chucvu':user.chucvu})
            return HttpResponse(data,content_type="application/json")
    return HttpResponse(json.dumps({'code': 0, 'status': 'Không có dữ liệu'}),content_type="application/json")

@csrf_exempt
def api_edit(request):
    if request.method == "POST":
        username = request.POST.get('username')
        ten = request.POST.get('ten')
        diachi = request.POST.get('diachi')
        SDT = request.POST.get('SDT')
        gioitinh = request.POST.get('gioitinh')
        chucvu = request.POST.get('chucvu')
        if utils.EditAPI(username,ten,diachi,SDT,gioitinh,chucvu).save():
            data = json.dumps({'code': 1, 'status': 'Sửa thành công'})    # trả lại token
            return HttpResponse(data,content_type="application/json")
    return HttpResponse(json.dumps({'code': 0, 'status': 'Không có dữ liệu'}),content_type="application/json")

@csrf_exempt
def api_makeNum(request):
    if request.method == "POST":
        token = request.POST.get('token')
        if utils.isAdminFromToken(token) == False:
            data = json.dumps({'code': 0, 'status': 'Tên đăng nhập hoặc mật khẩu sai hoặc không có quyền'})
            return HttpResponse(data,content_type="application/json")
        id_sp = int(request.POST.get('id'))
        m = int(request.POST.get('m'))
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
        result = utils.insertDataDinhDanh(id_sp,code_list,m,num_sum)
        if result == False:
            data = json.dumps({'code': 0, 'status': 'Tạo số không thành công'})
            return HttpResponse(data,content_type="application/json")
        data = json.dumps({'group2_list':group2_list,'code_list':code_list,'year':year,'group3':group3})
        return HttpResponse(data,content_type="application/json")
    return HttpResponse(json.dumps({'code': 0, 'status': 'Không có dữ liệu'}),content_type="application/json")


@csrf_exempt
def api_insertData(request):
    if request.method == "POST":
        token = request.POST.get('token')
        if utils.isAdminFromToken(token) == False:
            data = json.dumps({'code': 0, 'status': 'Tên đăng nhập hoặc mật khẩu sai hoặc không có quyền'})
            return HttpResponse(data,content_type="application/json")
        # id = int(request.POST.get('id'))
        ten = request.POST.get('ten')
        gia = request.POST.get('gia')
        result = utils.insert(ten, gia)
        if result==False:
            return HttpResponse({'Thêm dữ liệu không thành công'})
        data = json.dumps({'ten':ten,'gia':gia})
        return HttpResponse(data,content_type="application/json")
    return HttpResponse(json.dumps({'code': 0, 'status': 'Không có dữ liệu'}),content_type="application/json")


@csrf_exempt
def api_findData(request):
    key = ""
    label = "id"
    if request.method == "POST":
        label = request.POST.get('label')
        key = request.POST.get('key')
        # print(label)
        # print(key)
    if key != "" and key!=None:
        data = utils.find(label, key)  # trả lại dưới dạng đổi tượng sql
        # cần chuyển về dạng danh sách
        data_re = []
        for i in data:
            # print(i)
            element = {"id":str(i.id),"ten":i.ten,"gia":int(i.gia)}
            data_re.append(element)
        data_re = json.dumps(data_re)       # chuyển dữ liệu về dạng json
        return HttpResponse(data_re,content_type="application/json")
    return HttpResponse(json.dumps({'code': 0, 'status': 'Không có dữ liệu'}),content_type="application/json")

@csrf_exempt
def api_findDataMa(request):
    if request.method == "POST":
        ma_dd = request.POST.get('ma_dd')
        id = utils.findMa(ma_dd)
        if id == False:
            data = json.dumps({'code': 0, 'status': 'Không có thông tin'})
            return HttpResponse(data,content_type="application/json")
        data = utils.find("id",str(id))
        data_re = []
        for i in data:
            element = {"id": str(i.id), "ten": i.ten, "gia": int(i.gia)}
            data_re.append(element)
        data_re = json.dumps(data_re)  # chuyển dữ liệu về dạng json
        return HttpResponse(data_re, content_type="application/json")
    return HttpResponse(json.dumps({'code': 0, 'status': 'Không có dữ liệu'}),content_type="application/json")
