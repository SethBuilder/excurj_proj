# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excurj', '0042_auto_20170517_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestreference',
            name='traveler_fun',
            field=models.BooleanField(default=True),
        ),
    ]
