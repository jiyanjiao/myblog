from django.db import models
import time
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.CharField(max_length=32, default='content')
    create_time = models.DateTimeField(default=time.time(), verbose_name="更新时间")
    
    def __str__(self):
        return self.title
