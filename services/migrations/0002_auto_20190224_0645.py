# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-24 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Works',
        ),
        migrations.RenameField(
            model_name='generalpurpose',
            old_name='services',
            new_name='works',
        ),
    ]
