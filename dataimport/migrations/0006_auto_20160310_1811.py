# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-10 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_auto_20160310_1811'),
        ('dataimport', '0005_auto_20160302_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorDetailFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='Indicator_Detail_Information')),
                ('state_indicator', models.BooleanField(default=False)),
                ('district_indicator', models.BooleanField(default=False)),
                ('school_indicator', models.BooleanField(default=False)),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.SchoolYear')),
            ],
        ),
        migrations.AlterField(
            model_name='districtfield',
            name='match_option',
            field=models.CharField(blank=True, choices=[('STATE_CODE', 'state_code'), ('DISTRICT_CODE', 'district_code (required)'), ('DISTRICT_NAME', 'district_name'), ('ADDRESS', 'address'), ('CITY', 'city'), ('STATE', 'state'), ('ZIP', 'zip'), ('PHONE', 'phone'), ('WEB_SITE', 'web_site'), ('SUPERINTENDENT', 'Superintendent'), ('DESCRIPTION', 'Description'), ('NUMBER_STUDENT', 'number of student'), ('NUMBER_TEACHER', 'number of teacher')], help_text='(required) Select district_code, district_name, address, city, state, zip, phone, web_site, superintendent', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='indicatorfield',
            name='match_option',
            field=models.CharField(blank=True, choices=[('STATE_CODE', 'state_code (required pick one)'), ('DISTRICT_CODE', 'district_code (required pick one)'), ('SCHOOL_CODE', 'school_code (required pick one)'), ('DIMENSION', 'dimension')], help_text='(required)', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='schoolfield',
            name='match_option',
            field=models.CharField(blank=True, choices=[('DISTRICT_CODE', 'district_code'), ('PRINCIPAL', 'principal'), ('SCHOOL_CODE', 'school_code (required)'), ('SCHOOL_NAME', 'school_name'), ('SCHOOL_TYPE', 'school_type'), ('GRADE_TYPE', 'grade_type'), ('ADDRESS', 'address'), ('CITY', 'city'), ('STATE', 'state'), ('ZIP', 'zip'), ('PHONE', 'phone'), ('WEB_SITE', 'web_site'), ('LOW_GRADE', 'low_grade'), ('HIGH_GRADE', 'high_grade'), ('DESCRIPTION', 'Description'), ('NUMBER_STUDENT', 'number of student'), ('NUMBER_TEACHER', 'number of teacher')], help_text='(required) [low_grade and high_grade only accept PK, K, and 1 - 12] [grade_type only accept "Emh"]', max_length=30, null=True),
        ),
    ]
