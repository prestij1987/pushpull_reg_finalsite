from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='photo/')
    book = models.FileField(upload_to='note/')

    def __str__(self):
        return self.title
    

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Books(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to=user_directory_path)
    book = models.FileField(upload_to='books/%Y-%m-%d/')



class MyModel(models.Model):
    ...
    upload = models.FileField(upload_to=user_directory_path)    

class Voice(models.Model):
    # Указывает на абсолютный путь
    audio = models.FilePathField(path='/home/user/')    