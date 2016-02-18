# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 22:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('day', models.DateField(default=datetime.datetime.now, unique=True)),
                ('daily_goal', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(blank=True, max_length=600, null=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Day')),
            ],
        ),
    ]