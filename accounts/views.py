from django.shortcuts import render,redirect
from .forms import RegistrationForm
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
            respone = HttpResponse("vua tao xong")
            return respone
    return render(request,'pages/register.html',{'form':form})
def home(request):
    if(request.session.session_key):
        return render(request,'pages/index.html')
    else:
        return redirect('/register')