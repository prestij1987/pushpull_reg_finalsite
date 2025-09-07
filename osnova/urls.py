from django.urls import path
from .views import show, show_new

urlpatterns = [
    path('', show, name='home'),
    #path('mystring/', func_start, name='mystring')
    path('start/', show_new, name='head_main' )
    
]