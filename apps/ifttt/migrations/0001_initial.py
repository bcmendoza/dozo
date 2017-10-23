# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 19:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifttt_id', models.CharField(max_length=8)),
                ('connected', models.BooleanField(default=False)),
                ('in_session', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_date', models.DateTimeField()),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
