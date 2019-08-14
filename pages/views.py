from django.shortcuts import render
import random

# Create your views here.
# 중요함 ㅋㅋㅋ 특정로직 담당

def index(request):     #첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보
    return render(request, 'index.html') #render에 첫번째 인자도 request


def introduce(request):
    return render(request, 'introduce.html')


# template variable example
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name,
    }
    # django template 으로 context 전달
    return render(request, 'dinner.html', context)


def image(request):
    img = 'https://picsum.photos/500'
    context = {
        'img': img,
    }
    return render(request, 'image.html', context)


def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    context = {
        'result': num1 * num2,
        'num1': num1,
        'num2': num2,
    }
    return render(request, 'times.html', context)
