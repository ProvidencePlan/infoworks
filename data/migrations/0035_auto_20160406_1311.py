# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-06 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0034_auto_20160331_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtovertime',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], default='NUMERIC', max_length=7),
        ),
        migrations.AddField(
            model_name='districtovertime',
            name='y_axis_title_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='districtovertimeelement',
            name='display_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='schoolovertime',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], default='NUMERIC', max_length=7),
        ),
        migrations.AddField(
            model_name='schoolovertime',
            name='y_axis_title_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='schoolovertimeelement',
            name='display_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='stateovertime',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], default='NUMERIC', max_length=7),
        ),
        migrations.AddField(
            model_name='stateovertime',
            name='y_axis_title_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='stateovertimeelement',
            name='display_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='districtindicatordata',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], max_length=20),
        ),
        migrations.AlterField(
            model_name='districtindicatordataset',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], default='STRING', max_length=7),
        ),
        migrations.AlterField(
            model_name='districtindicatordetaildata',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], max_length=7),
        ),
        migrations.AlterField(
            model_name='schoolindicatordata',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], max_length=7),
        ),
        migrations.AlterField(
            model_name='schoolindicatordataset',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], default='STRING', max_length=7),
        ),
        migrations.AlterField(
            model_name='schoolindicatordetaildata',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], max_length=7),
        ),
        migrations.AlterField(
            model_name='stateindicatordata',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], max_length=7),
        ),
        migrations.AlterField(
            model_name='stateindicatordataset',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], default='STRING', max_length=7),
        ),
        migrations.AlterField(
            model_name='stateindicatordetaildata',
            name='data_type',
            field=models.CharField(choices=[('NUMERIC', 'numeric'), ('PERCENT', 'percent'), ('STRING', 'string')], max_length=7),
        ),
    ]