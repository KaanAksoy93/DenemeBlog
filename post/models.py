from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title      = models.CharField(max_length=120, verbose_name="Title")
    content       = models.TextField(verbose_name="Content")
    publishingdate = models.DateTimeField(verbose_name="Publishing Date", auto_now_add=True)

    def __str__(self):   #show us the entered post name
        return self.title

    def get_absolute_url(self):

        return  reverse('post:detail', kwargs={'id': self.id})

        # return "/post/{}".format(self.id)