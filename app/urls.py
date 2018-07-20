from django.urls import path
from . import views
from . import apis
urlpatterns = [
    # path('find', views.findByKeyWeb),
    # path('phantrang', views.phantrang),
    # path('api/find', views.findByKeyAPI),
    path('make', views.makeNum),
    path('insert',views.insertData),
    path('find',views.findData),
    path('findma', views.findDataMa),
    path('listma', views.listMa),
    path('api/make', apis.api_makeNum),
    path('api/insert', apis.api_insertData),
    path('api/find', apis.api_findData),
    path('api/findma', apis.api_findDataMa),
    path('api/login', apis.api_login),
    path('api/verify', apis.api_verifyToken),
    path('api/edit', apis.api_edit),

]