# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 19:42
from __future__ import unicode_literals

import apps.landing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=45, validators=[apps.landing.models.lenLessThanThree])),
                ('last_name', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45, unique=True, validators=[apps.landing.models.lenLessThanThree])),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=100, validators=[apps.landing.models.lenLessThanEight])),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_online', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
