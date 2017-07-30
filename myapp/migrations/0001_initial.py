# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crossing1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('density', models.CharField(default='low density', max_length=30)),
                ('stray', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mapp',
            fields=[
                ('camera_id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('light_id', models.CharField(max_length=100, unique='True')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='crossing1',
            name='camera_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Mapp'),
        ),
    ]