# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 12:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excurj', '0024_auto_20170515_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 16, 15, 45, 33, 451606)),
        ),
    ]