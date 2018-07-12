from django import forms
import re
from .models import *


class RegistrationForm(forms.Form):
    username= forms.CharField(label="Tài khoản",max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Mật khẩu",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Nhập lại mật khẩu",widget=forms.PasswordInput())
    ten = forms.CharField(max_length=50, label="Tên")
    diachi = forms.CharField(max_length=50, label="Địa chỉ")
    SDT = forms.CharField(max_length=50, label="Số điện thoại")
    gioitinh = forms.CharField(max_length=10, label="giới tính")
    chucvu = forms.CharField(max_length=20, label="chức vụ")
    def clean_password2(self):      # kiểm tra 2 mật khẩu có giống nhau ko
        if 'password1' in self.cleaned_data:                # kiểm tra xem đã nhập password1 chưa
            pass1 = self.cleaned_data['password1']
            pass2 = self.cleaned_data['password2']
            print(pass1)
            print(pass2)
            if pass1 == pass2 and pass1:                # kiểm tra 2 mật khẩu có giống nhau không
                return pass2
        raise forms.ValidationError("Mật khẩu không hợp lệ")
    def clean_username(self):       # kiểm tra user có tồn tại ko
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        try:
            User.objects.get(username=username)
        except:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    def save(self):
#        print("Lưu user")
        user = User.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password1'],
                                 # ten=self.cleaned_data['ten'],
                                 #    diachi=self.cleaned_data['diachi'],
                                 #    SDT=self.cleaned_data['SDT'],
                                 #    gioitinh=self.cleaned_data['gioitinh'],
                                 #    chucvu=self.cleaned_data['chucvu']
                                 )
        user.ten=self.cleaned_data['ten']
        user.diachi=self.cleaned_data['diachi']
        user.SDT=self.cleaned_data['SDT']
        user.gioitinh=self.cleaned_data['gioitinh']
        user.chucvu=self.cleaned_data['chucvu']
        user.save()

class EditForm(forms.Form):
    username = forms.CharField(label="Tài khoản", max_length=30)
    # email = forms.EmailField(label="Email",required=False)
    ten = forms.CharField(max_length=50, label="Tên",required=False)
    diachi = forms.CharField(max_length=50, label="Địa chỉ",required=False)
    SDT = forms.CharField(max_length=50, label="Số điện thoại",required=False)
    gioitinh = forms.CharField(max_length=10, label="giới tính",required=False)
    chucvu = forms.CharField(max_length=20, label="chức vụ",required=False)

    def clean_username(self):  # kiểm tra user có tồn tại ko
        username = self.cleaned_data['username']
        print("form check save : #########: " +username)

        try:
            User.objects.get(username=username)
        except:
            raise forms.ValidationError("Tài khoản không tồn tại")
        return username

    def save(self):
        #        print("Lưu user")
        username = str(self.cleaned_data['username'])
        # print("form edit save : #########: " +username)
        try:
            user = User.objects.get(username=username)
            # print(user.username)
            # print(user.email)
        except:
            raise forms.ValidationError("Tài khoản không tồn tại")
        user.ten = self.cleaned_data['ten']
        user.diachi = self.cleaned_data['diachi']
        user.SDT = self.cleaned_data['SDT']
        user.gioitinh = self.cleaned_data['gioitinh']
        user.chucvu = self.cleaned_data['chucvu']
        user.save()
