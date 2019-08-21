"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# include모듈 사용하여 다른 어플로 보낸다
# 중요함 ㅋㅋㅋ  사용자가 들어올수 있는 경로 설정
# 정의x 경로 라면 404 not found
urlpatterns = [
    #path('사용자가 접속하는 경로', )
    # include모듈 사용하여 다른 어플로 보낸다
    path('pages/', include('pages.urls')),
    path('utilities/', include('utilities.urls')),
    path('admin/', admin.site.urls),
]

