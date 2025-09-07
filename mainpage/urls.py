

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',             views.index,      name='home'),
    path('uslugi/',      views.uslugi,     name='uslugi'),
    path('park/',        views.park,       name='park'),
    path('ing/',         views.ing,        name='ing'),
    path('otzyvi/',      views.otzyv,      name='otzyvi'),
    path('formaotvet/',  views.formaotvet, name='formaotvet'),
    path('work/', views.work, name='work'),
    path('zimnik/', views.zimnik, name='zimnik'),
    
    #path('mystring/', func_start, name='mystring'),
    
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
