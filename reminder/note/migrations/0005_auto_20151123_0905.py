# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20151123_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='tag',
            field=models.ManyToManyField(to='note.Tags', blank=True),
        ),
    ]
