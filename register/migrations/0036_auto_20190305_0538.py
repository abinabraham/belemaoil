# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0035_auto_20190305_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredoffice',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_ofc', to='register.ContractorModel'),
        ),
        migrations.AlterField(
            model_name='website',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_website', to='register.ContractorModel'),
        ),
    ]
