# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-18 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0023_auto_20190218_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='no_of_staff',
            field=models.CharField(choices=[('0 - 10', '0 - 10'), ('10 - 20', '10 - 20')], max_length=75),
        ),
    ]