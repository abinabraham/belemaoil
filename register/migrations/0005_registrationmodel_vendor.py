# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-17 13:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_contactdetailsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='vendor',
            field=models.CharField(default=datetime.datetime(2019, 2, 17, 13, 44, 41, 302888), max_length=45),
            preserve_default=False,
        ),
    ]
