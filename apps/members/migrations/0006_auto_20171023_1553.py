# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_assignment_goal_profile_session'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Goal',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='member',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
