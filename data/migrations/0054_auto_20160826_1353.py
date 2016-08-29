# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-26 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0053_auto_20160824_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtindicator',
            name='highchart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.DistrictDisplayDataYDetail'),
        ),
        migrations.AddField(
            model_name='schoolindicator',
            name='highchart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.SchoolDisplayDataYDetail'),
        ),
        migrations.AddField(
            model_name='stateindicator',
            name='highchart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.StateDisplayDataYDetail'),
        ),
        migrations.AlterField(
            model_name='districtdisplaydataydetailset',
            name='display_type',
            field=models.CharField(choices=[('BAR-CHART', 'Bar Chart'), ('BAR-CHART-ONLY', 'Bar Chart Only'), ('GROUPED-COLUMN', 'Grouped Column Chart'), ('HORZ-BAR-CHART', 'Horizontal Bar Chart'), ('HORZ-BAR-CHART-ONLY', 'Horizontal Bar Chart Only'), ('LINE-CHART', 'Line Chart (under construction)'), ('AREA-CHART', 'Area Chart (under construction)'), ('PIE-CHART', 'Pie Chart'), ('TABLE', 'Table')], max_length=20),
        ),
        migrations.AlterField(
            model_name='districtindicatordetaildataset',
            name='display_type',
            field=models.CharField(choices=[('BAR-CHART', 'Bar Chart'), ('BAR-CHART-ONLY', 'Bar Chart Only'), ('GROUPED-COLUMN', 'Grouped Column Chart'), ('HORZ-BAR-CHART', 'Horizontal Bar Chart'), ('HORZ-BAR-CHART-ONLY', 'Horizontal Bar Chart Only'), ('LINE-CHART', 'Line Chart (under construction)'), ('AREA-CHART', 'Area Chart (under construction)'), ('PIE-CHART', 'Pie Chart'), ('TABLE', 'Table')], max_length=20),
        ),
        migrations.AlterField(
            model_name='districtovertime',
            name='chart_type',
            field=models.CharField(choices=[('BAR-CHART', 'Bar Chart'), ('BAR-CHART-ONLY', 'Bar Chart Only'), ('GROUPED-COLUMN', 'Grouped Column Chart'), ('HORZ-BAR-CHART', 'Horizontal Bar Chart'), ('HORZ-BAR-CHART-ONLY', 'Horizontal Bar Chart Only'), ('LINE-CHART', 'Line Chart (under construction)'), ('AREA-CHART', 'Area Chart (under construction)'), ('PIE-CHART', 'Pie Chart'), ('TABLE', 'Table')], default='BAR-CHART', max_length=50),
        ),
        migrations.AlterField(
            model_name='schooldisplaydataydetailset',
            name='display_type',
            field=models.CharField(choices=[('BAR-CHART', 'Bar Chart'), ('BAR-CHART-ONLY', 'Bar Chart Only'), ('GROUPED-COLUMN', 'Grouped Column Chart'), ('HORZ-BAR-CHART', 'Horizontal Bar Chart'), ('HORZ-BAR-CHART-ONLY', 'Horizontal Bar Chart Only'), ('LINE-CHART', 'Line Chart (under construction)'), ('AREA-CHART', 'Area Chart (under construction)'), ('PIE-CHART', 'Pie Chart'), ('TABLE', 'Table')], max_length=20),
        ),
        migrations.AlterField(
            model_name='schoolindicatordetaildataset',
            name='display_type',
            field=models.CharField(choices=[('BAR-CHART', 'Bar Chart'), ('BAR-CHART-ONLY', 'Bar Chart Only'), ('GROUPED-COLUMN', 'Grouped Column Chart'), ('HORZ-BAR-CHART', 'Horizontal Bar Chart'), ('HORZ-BAR-CHART-ONLY', 'Horizontal Bar Chart Only'), ('LINE-CHART', 'Line Chart (under construction)'), ('AREA-CHART', 'Area Chart (under construction)'), ('PIE-CHART', 'Pie Chart'), ('TABLE', 'Table')], max_length=20),
        ),
        migrations.AlterField(
            model_name='schoolovertime',
            name='chart_type',
            field=models.CharField(choices=[('BAR-CHART', 'Bar Chart'), ('BAR-CHART-ONLY', 'Bar Chart Only'), ('GROUPED-COLUMN', 'Grouped Column Chart'), ('HORZ-BAR-CHART', 'Horizontal Bar Chart'), ('HORZ-BAR-CHART-ONLY', 'Horizontal Bar Chart Only'), ('LINE-CHART', 'Line Chart (under construction)'), ('AREA-CHART', 'Area Chart (under construction)'), ('PIE-CHART', 'Pie Chart'), ('TABLE', 'Table')], default='BAR-CHART', max_length=50),
        ),
        migrations.AlterField(
            model_name='statedisplaydataydetailset',
            name='display_type',
            field=models.CharField(choices=[('BAR-CHART', 'Bar Chart'), ('BAR-CHART-ONLY', 'Bar Chart Only'), ('GROUPED-COLUMN', 'Grouped Column Chart'), ('HORZ-BAR-CHART', 'Horizontal Bar Chart'), ('HORZ-BAR-CHART-ONLY', 'Horizontal Bar Chart Only'), ('LINE-CHART', 'Line Chart (under construction)'), ('AREA-CHART', 'Area Chart (under construction)'), ('PIE-CHART', 'Pie Chart'), ('TABLE', 'Table')], max_length=20),
        ),
        migrations.AlterField(
            model_name='stateindicatordetaildataset',
            name='display_type',
            field=models.CharField(choices=[('BAR-CHART', 'Bar Chart'), ('BAR-CHART-ONLY', 'Bar Chart Only'), ('GROUPED-COLUMN', 'Grouped Column Chart'), ('HORZ-BAR-CHART', 'Horizontal Bar Chart'), ('HORZ-BAR-CHART-ONLY', 'Horizontal Bar Chart Only'), ('LINE-CHART', 'Line Chart (under construction)'), ('AREA-CHART', 'Area Chart (under construction)'), ('PIE-CHART', 'Pie Chart'), ('TABLE', 'Table')], max_length=20),
        ),
        migrations.AlterField(
            model_name='stateovertime',
            name='chart_type',
            field=models.CharField(choices=[('BAR-CHART', 'Bar Chart'), ('BAR-CHART-ONLY', 'Bar Chart Only'), ('GROUPED-COLUMN', 'Grouped Column Chart'), ('HORZ-BAR-CHART', 'Horizontal Bar Chart'), ('HORZ-BAR-CHART-ONLY', 'Horizontal Bar Chart Only'), ('LINE-CHART', 'Line Chart (under construction)'), ('AREA-CHART', 'Area Chart (under construction)'), ('PIE-CHART', 'Pie Chart'), ('TABLE', 'Table')], default='BAR-CHART', max_length=50),
        ),
    ]