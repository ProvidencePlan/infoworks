# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-23 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataimport', '0012_auto_20160323_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimensionname',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]