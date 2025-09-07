from django.contrib import admin
from .models import Task, Dist

@admin.register(Dist)
class DistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dist._meta.get_fields()]


@admin.register(Task)
class DistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.get_fields()]  



#admin.site.register(Task)
#admin.site.register(Dist)

