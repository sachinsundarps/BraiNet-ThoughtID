# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-29 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='user_name')),
                ('brain_signal', models.CharField(blank=True, max_length=200, null=True, verbose_name='brain_signal')),
            ],
        ),
    ]
