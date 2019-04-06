# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-02 00:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='good',
        ),
        migrations.AddField(
            model_name='category',
            name='create_user',
            field=models.OneToOneField(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='created_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='good',
            name='category',
            field=models.OneToOneField(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Category'),
        ),
    ]