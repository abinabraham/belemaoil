# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-20 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0025_auto_20190220_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='country_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='register.CountryCodeMaster'),
        ),
    ]
