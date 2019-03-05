# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0034_auto_20190305_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_email', to='register.ContractorModel'),
        ),
    ]
