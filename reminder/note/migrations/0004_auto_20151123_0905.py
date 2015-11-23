# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20151120_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notes',
            name='category',
            field=models.ManyToManyField(to='note.Categories', blank=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='color',
            field=models.ForeignKey(blank=True, to='note.Colors', null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='tag',
            field=models.ManyToManyField(to='note.Tags', null=True, blank=True),
        ),
    ]
