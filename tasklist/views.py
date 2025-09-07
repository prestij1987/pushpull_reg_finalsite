from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
#from .templates.tasklist import index

# Create your views here.

def func_start(request):
    return render(request, 'index.html')

# Вытащить все обьекты из бд типа Task
#print('index.html')


def index(request):
    tasks = Task.objects.all()
    # tasks = Task.objects.all()
# Вытащить все обьекты из бд типа Task
    context = {
        'kogda': 'segonya',
        'tasks': tasks
    }
    return render(
        request,   # zapros
        'tasklist/first.html',  # put k shablonu
                                # podstanovka
        context
    )



'''from .models import Kitten
def look_for(request):
    if request.method == "POST":
#       form = KittenForm(request.POST, request.FILES)
        print(request.POST)
   #     print(request.POST['Catname'][0])
        print(request.POST.get('Catname'))
        context = {'kotenok': 'Котята не найдены'}
        kittens_found = Kitten.objects.filter(imya=request.POST.get('Catname'))
        if kittens_found: #Если котята найдены, список QuerySet [] не будет пустым и не будет ложным, в питоне все пустое - ложное, но не является False!
            context = {
                'kotenok': Kitten.objects.get(imya=request.POST.get('Catname'))
            }
        else:
            print('проверка котенка', Kitten.objects.filter(imya=request.POST.get('Catname')))
'''
