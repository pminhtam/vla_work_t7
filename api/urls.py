from django.urls import path
from . import views
urlpatterns = [
    # path('find', views.findByKeyWeb),
    # path('phantrang', views.phantrang),
    # path('api/find', views.findByKeyAPI),
    path('make', views.makeNum),
    path('insert',views.insertData),
    path('find',views.findData),
    path('findma', views.findDataMa),
    path('api/make', views.api_makeNum),
    path('api/insert', views.api_insertData),
    path('api/find', views.api_findData),
    path('api/findma', views.api_findDataMa),
    path('api/login', views.api_login),
    path('api/verify', views.api_verifyToken),
    path('api/edit', views.api_edit),

]