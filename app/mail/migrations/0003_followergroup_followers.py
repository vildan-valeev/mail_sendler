# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-03-23 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20220323_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='followergroup',
            name='followers',
            field=models.ManyToManyField(related_name='groups', to='mail.Follower'),
        ),
    ]
