# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-07 20:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front_page', '0002_auto_20160304_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
