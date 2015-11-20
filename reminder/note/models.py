from django.db import models
from django.contrib.auth.models import User

import mptt


# Create your models here.
class Colors(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="parent", related_name='child')
    author = models.ForeignKey(User)


    def __unicode__(self):
        return self.name


class Notes(models.Model):
    name = models.CharField(max_length=100)
    context = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    color = models.ForeignKey(Colors)
    tag = models.ManyToManyField(Tags)
    category = models.ManyToManyField(Categories)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

mptt.register(Categories,)
