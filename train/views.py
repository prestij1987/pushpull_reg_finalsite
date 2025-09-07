from django.shortcuts import render
from django.http import HttpRequest
from .data_dela import work_data
from datetime import datetime
# Create your views here.


'''def func_start(response):
    return HttpRequest('My two string')
print('index.html')'''


def index(request):
   
    tasks = [
        'Рассказать урок',
        'Дать задание',
        'Проверить задани',
        'Объяснить домашку',
    ]
    context = {
        'kogda': work_data(datetime(2024, 5, 28)),
    }  
    return render(
        request,                # Запрос
	    'tasklist/first.html',  # путь к шаблону
        context                 # подстановки
        
    )