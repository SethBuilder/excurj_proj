# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-25 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excurj', '0046_auto_20170524_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city_text',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]