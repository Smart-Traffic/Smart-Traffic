# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 05:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20170730_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stray1',
            name='cam_id',
        ),
        migrations.DeleteModel(
            name='Stray1',
        ),
    ]