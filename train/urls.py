
from django.urls import path
from .views import index
#from .views import func_start

urlpatterns = [
    path('', index, name='home'),
    #path('mystring/', func_start, name='mystring')
    
]
