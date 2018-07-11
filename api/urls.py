from django.urls import path
from . import views
urlpatterns = [
    # path('find', views.findByKeyWeb),
    # path('phantrang', views.phantrang),
    # path('api/find', views.findByKeyAPI),
    path('make', views.makeNum),
    path('insert',views.insertData),
    path('find',views.findData),
    path('api/make', views.api_makeNum),
    path('api/insert', views.api_insertData),
    path('api/find', views.api_findData),
]