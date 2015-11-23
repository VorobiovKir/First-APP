# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20151123_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='child', verbose_name=b'parent', blank=True, to='note.Categories', null=True),
        ),
    ]
