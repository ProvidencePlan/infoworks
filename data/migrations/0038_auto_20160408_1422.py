# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-08 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0037_customdimensionyname_is_positive'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtdisplaydataydetailset',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], default='PERCENT', max_length=7),
        ),
        migrations.AddField(
            model_name='schooldisplaydataydetailset',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], default='PERCENT', max_length=7),
        ),
        migrations.AddField(
            model_name='statedisplaydataydetailset',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], default='PERCENT', max_length=7),
        ),
    ]