# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-02 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20160301_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='us_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.State'),
        ),
    ]
