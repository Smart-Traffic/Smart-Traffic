# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_crossing1_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stray1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stray', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='crossing1',
            old_name='cam',
            new_name='cam_id',
        ),
        migrations.RenameField(
            model_name='crossing1',
            old_name='conclusion',
            new_name='density',
        ),
        migrations.RemoveField(
            model_name='crossing1',
            name='stray',
        ),
        migrations.AlterField(
            model_name='mapp',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='stray1',
            name='cam_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Mapp'),
        ),
    ]
