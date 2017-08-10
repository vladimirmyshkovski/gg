# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 14:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20170807_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 9, 14, 6, 38, 776767, tzinfo=utc)),
        ),
    ]