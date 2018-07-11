from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not email:
            raise ValueError('Bạn phải điền email vào')
        elif not username:
            raise ValueError('Bạn phải có username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.is_superuser = False

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',unique=True)
    username = models.CharField(max_length=50,unique=True)
    ten = models.CharField(max_length=50,blank=True,verbose_name="Tên")
    diachi = models.CharField(max_length=50,blank=True,verbose_name="Địa chỉ")
    SDT = models.CharField(max_length=50,blank=True,verbose_name="Số điện thoại")
    gioitinh = models.CharField(max_length=10,blank=True,verbose_name="giới tính")
    chucvu = models.CharField(max_length=20,blank=True,verbose_name="chức vụ")

    is_superuser = models.BooleanField(default=False,null=True)

    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.ten
    def get_short_name(self):
        return self.ten
    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_superuser