# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-03-23 06:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followergroup',
            name='followers',
        ),
        migrations.AddField(
            model_name='follower',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mail.FollowerGroup'),
            preserve_default=False,
        ),
    ]
