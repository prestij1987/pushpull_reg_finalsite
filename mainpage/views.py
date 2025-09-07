from django.shortcuts import render
from django.conf import settings
from datetime import datetime


def index(request):
    context = {}
    return render(
        request,   # zapros
        'mainpage/index.html',  # put k shablonu
                                # podstanovka
        context
    )


def uslugi(request):
    context = {}
    return render(
        request,   # zapros
        'mainpage/html/uslugi.html',  # put k shablonu
                                # podstanovka
        context
    )

def ing(request):
    context = {}
    return render(
        request,   # zapros
        'mainpage/html/ing.html',  # put k shablonu
                                # podstanovka
        context
    )


def park(request):
    context = {'park techniki' : 'Чертежи и схемы тралов'}
    return render(request,   
        'mainpage/html/park.html',  
                               
        context
    )

def work(request):
    context = {'Фото выполненных работ' : 'dist'}
    return render(request,   
        'mainpage/html/work.html',  
                               
        context
    )



def otzyv(request):
    if request.method == "POST":
        otzyv_num = datetime.now().strftime('%Y%m%d%H%M%S.txt')
        f = open(
            settings.BASE_DIR / 'mainpage/templates/mainpage/otzyv/' / otzyv_num,
            'w', encoding="utf-8")
        f.write(request.POST['theme'] + '\n\n' + request.POST['txt'])
        f.close()
        return render(
            request,
            'mainpage/html/otzyvsaved.html',
            context = {'otzyv_num': otzyv_num}
            )
    context = {}
    return render(request,   
        'mainpage/html/otzyvi.html',  
                               
        context
    )

def formaotvet(request):
    context = {}
    return render(
        request,
        'mainpage/html/formaotvet.html',
        context
    )

def zimnik(request):
    context = {}
    return render(
        request,
        'mainpage/html/zimnik.html',
        context
    )