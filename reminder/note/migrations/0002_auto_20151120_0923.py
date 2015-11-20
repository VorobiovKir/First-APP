# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='author',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='notes',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
