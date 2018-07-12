from django.shortcuts import render,redirect
from .forms import RegistrationForm,EditForm
from django.http import HttpResponse
from .models import User
# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("is_valid()")
            form.save()
            # return HttpResponseRedirect("/")
            # respone = HttpResponse("vua tao xong")
            # return respone
            return render(request, 'pages/error.html', {'data': 'Tạo tài khoản thành công, bạn có thể đăng nhập'})
    return render(request,'pages/register.html',{'form':form})

def home(request):
    if(request.session.session_key):
        return render(request,'pages/index.html')
    else:
        return redirect('/login')

def edit(request):
    if(request.user.is_anonymous):
        # return HttpResponse("Chưa đăng nhập")
        return render(request,'pages/error.html',{'data':'Bạn phải đăng nhập'})
    form = EditForm()
    if request.method == "POST":
        print(request.POST.get('username'))
        form = EditForm(request.POST)
        if form.is_valid():
            # print("is_valid()")
            form.save()
            # return HttpResponseRedirect("/")
            # respone = HttpResponse("vua sua xong")
            # return respone
            return render(request, 'pages/error.html', {'data': 'Sửa thông tin thành công'})
    return render(request,'pages/edit.html',{'form':form})