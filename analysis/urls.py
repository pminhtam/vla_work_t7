from django.urls import path
from . import views
urlpatterns = [
    path('code', views.codeAnalysis),
    path('price', views.price),
    path('history', views.history),
]