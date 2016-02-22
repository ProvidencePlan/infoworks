# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimensionFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DimensionName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('match_option', models.CharField(blank=True, choices=[('DISTRICT_CODE', 'district_code'), ('DISTRICT_NAME', 'district_name'), ('ADDRESS', 'address'), ('CITY', 'city'), ('STATE', 'state'), ('ZIP', 'zip'), ('PHONE', 'phone'), ('WEB_SITE', 'web_site'), ('SUPERINTENDENT', 'Superintendent')], help_text='(required) Select district_code, district_name, address, city, state, zip, phone, web_site, superintendent', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='District_Information')),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.SchoolYear')),
            ],
        ),
        migrations.CreateModel(
            name='IndicatorField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('match_option', models.CharField(blank=True, choices=[('DISTRICT_CODE', 'district_code'), ('SCHOOL_CODE', 'school_code'), ('DIMENSION', 'dimension')], help_text='(required)', max_length=30, null=True)),
                ('data_type', models.CharField(blank=True, choices=[('NUMERIC', 'numeric'), ('STRING', 'string')], help_text='(required)', max_length=30, null=True)),
                ('dimension_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataimport.DimensionName')),
            ],
        ),
        migrations.CreateModel(
            name='IndicatorFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='Indicator_Information')),
                ('district_indicator', models.BooleanField(default=False)),
                ('school_indicator', models.BooleanField(default=False)),
                ('indicator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.IndicatorTitle')),
                ('indicator_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataimport.DimensionFor')),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.SchoolYear')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('match_option', models.CharField(blank=True, choices=[('DISTRICT_CODE', 'district_code'), ('PRINCIPAL', 'principal'), ('SCHOOL_CODE', 'school_code'), ('SCHOOL_NAME', 'school_name'), ('SCHOOL_TYPE', 'school_type'), ('GRADE_TYPE', 'grade_type'), ('ADDRESS', 'address'), ('CITY', 'city'), ('STATE', 'state'), ('ZIP', 'zip'), ('PHONE', 'phone'), ('WEB_SITE', 'web_site'), ('LOW_GRADE', 'low_grade'), ('HIGH_GRADE', 'high_grade')], help_text='(required) [low_grade and high_grade only accept PK, K, and 1 - 12] [grade_type only accept "Emh"]', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='School_Information')),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.SchoolYear')),
            ],
        ),
        migrations.AddField(
            model_name='schoolfield',
            name='school_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataimport.SchoolFile'),
        ),
        migrations.AddField(
            model_name='indicatorfield',
            name='indicator_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataimport.IndicatorFile'),
        ),
        migrations.AddField(
            model_name='districtfield',
            name='district_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataimport.DistrictFile'),
        ),
    ]
