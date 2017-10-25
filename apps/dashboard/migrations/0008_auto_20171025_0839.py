# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 12:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20171025_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='ttc',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='daily_avg',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='hrs_vs_est',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='weekly_avg',
        ),
        migrations.AddField(
            model_name='assignment',
            name='on_time',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scorecard',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scorecard',
            name='todays_actual',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scorecard',
            name='todays_potential',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scorecards', to=settings.AUTH_USER_MODEL),
        ),
    ]
