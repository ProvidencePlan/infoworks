# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-01 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0057_auto_20160829_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtdisplaydataysetting',
            name='prefix',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='districtdisplaydataysetting',
            name='suffix',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='schooldisplaydataysetting',
            name='prefix',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='schooldisplaydataysetting',
            name='suffix',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]