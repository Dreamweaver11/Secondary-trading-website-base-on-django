# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-08 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0003_auto_20190408_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='good_statuc',
            new_name='good_status',
        ),
    ]
