# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]