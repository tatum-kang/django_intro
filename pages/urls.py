from django.urls import path
#  . 은 현재 경로에서 부터 사용 
from . import views

urlpatterns = [
    path('num/push/', views.num_push),
    path('num/pull/', views.num_pull),
    path('static_example/', views.static_example),
    path('lotto_result/', views.lotto_result),
    path('lotto_pick/', views.lotto_pick),
    path('result/', views.result),
    path('search/', views.search),
    path('lotto/', views.lotto),
    path('isitbirthday/', views.isitbirthday),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
]
