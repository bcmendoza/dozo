# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_assignment_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.CharField(choices=[('a', 'listed'), ('b', 'agenda'), ('c', 'current'), ('d', 'done')], max_length=45),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='track',
            field=models.CharField(choices=[('PyFun', 'Python Fundamentals'), ('PyOOP', 'Python OOP'), ('Flask', 'Python: Flask')], max_length=45),
        ),
    ]
