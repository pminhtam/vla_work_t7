from django.urls import path
from . import views
from . import apis
urlpatterns = [
    path('code', views.codeAnalysis),
    path('price', views.price),
    path('history', views.history),
    path('api/code', apis.api_codeAnalysis),
    path('api/price', apis.api_price),
    path('api/history', apis.api_history),
]