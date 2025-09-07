from django.shortcuts import render

# Create your views here.

def show(request):
    return render(request, 'osnova/main.html')

def show_new(request):
    return render(request, 'osnova/start.html')