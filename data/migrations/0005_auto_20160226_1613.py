# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_districtdisplaydata_schooldisplaydata'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtdisplaydata',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='schooldisplaydata',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]