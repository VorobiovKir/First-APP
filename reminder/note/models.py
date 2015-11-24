from django.db import models
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey


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


class Categories(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', blank=True, null=True, verbose_name="parent", related_name='child')
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Notes(models.Model):
    name = models.CharField(max_length=100)
    context = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    color = models.ForeignKey(Colors, blank=True, null=True)
    tag = models.ManyToManyField(Tags, blank=True)
    category = models.ManyToManyField(Categories, blank=True)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
