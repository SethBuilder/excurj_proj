# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excurj', '0041_auto_20170517_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestreference',
            name='id',
        ),
        migrations.AlterField(
            model_name='requestreference',
            name='request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='excurj.Request'),
        ),
    ]
