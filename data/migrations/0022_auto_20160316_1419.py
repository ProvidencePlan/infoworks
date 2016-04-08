# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-16 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0021_districtdisplaydataydetaildata_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDimensionXName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomDimensionYName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='districtdisplaydataydetaildata',
            name='new_dimension_x_name',
        ),
        migrations.RemoveField(
            model_name='districtdisplaydataydetaildata',
            name='new_dimension_y_name',
        ),
    ]