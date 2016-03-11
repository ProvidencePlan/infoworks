# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-10 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_auto_20160310_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districtindicatordata',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('STRING', 'string'), ('SUBDATASET', 'subdataset')], max_length=20),
        ),
        migrations.AlterField(
            model_name='districtindicatordetaildataset',
            name='display_type',
            field=models.CharField(choices=[('BAR_CHART', 'Bar Chart'), ('PIE_CHART', 'Pie Chart'), ('SHOW_TABLE', 'Show Table')], max_length=20),
        ),
        migrations.AlterField(
            model_name='schoolindicatordetaildataset',
            name='display_type',
            field=models.CharField(choices=[('BAR_CHART', 'Bar Chart'), ('PIE_CHART', 'Pie Chart'), ('SHOW_TABLE', 'Show Table')], max_length=20),
        ),
        migrations.AlterField(
            model_name='stateindicatordetaildataset',
            name='display_type',
            field=models.CharField(choices=[('BAR_CHART', 'Bar Chart'), ('PIE_CHART', 'Pie Chart'), ('SHOW_TABLE', 'Show Table')], max_length=20),
        ),
    ]