# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170729_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapp',
            name='created_on',
            field=models.CharField(max_length=10),
        ),
    ]
