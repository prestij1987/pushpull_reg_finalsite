

from django.urls import path
from .views import register

urlpatterns = [
    path('', register, name='password'),
    #path('mystring/', func_start, name='mystring')
    #path('start/', '', name='head_main' )
    
]