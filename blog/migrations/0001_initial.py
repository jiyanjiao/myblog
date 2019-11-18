# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-11-15 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=32)),
                ('content', models.CharField(default='content', max_length=32)),
                ('create_time', models.DateTimeField(default=1573810566.05279, verbose_name='更新时间')),
            ],
        ),
    ]
