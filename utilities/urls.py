from django.urls import path
#  . 은 현재 경로에서 부터 사용 
from . import views

urlpatterns = [
    path('index/', views.index),
]
