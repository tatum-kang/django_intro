from django.shortcuts import render
from datetime import datetime
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


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)


def isitbirthday(request):
    context = {
        'birthday': datetime(2019,8,16)
    }
    return render(request, 'isitbirthday.html', context)


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    lotto = list(random.sample(range(1,46), 6))
    lotto.sort() #랜덤으로 뽑은 로또 번호
    context = {
        'real_lotto': real_lotto,
        'lotto': lotto
    }
    return render(request, 'lotto.html', context)


def search(request):
    return render(request, 'search.html')


def result(request):

    query = request.GET.get('query')
    category = request.GET.get('category')
    context = {
        'query': query,
        'category': category,
    }
    return render(request, 'result.html', context)
    

def lotto_pick(request):
    return render(request, 'lotto_pick.html')

def lotto_result(request):
    numbers = list(map(int, request.GET.get('numbers').strip().split()))
    numbers.sort()
    real_lotto = [21, 25, 30, 32, 40, 42]
    bonus_num = 38
    cnt = 0
    bonus = False
    for num in numbers:
        if num in real_lotto:
            cnt += 1
        if num == bonus_num:
            bonus = True

    context = {
        'numbers': numbers,
        'real_lotto': real_lotto,
        'cnt': cnt,
        'bonus': bonus
    }
    return render(request, 'lotto_result.html', context)

def static_example(request):
    return render(request, 'static_example.html')
