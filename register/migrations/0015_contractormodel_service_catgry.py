# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-18 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_contactpersondetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractormodel',
            name='service_catgry',
            field=models.CharField(choices=[('Equipment Lease', 'Equipment Lease'), ('Oil Tools', 'Oil Tools'), ('Technology', 'Technology'), ('Oil Well Servicing', 'Oil Well Servicing')], default=1, max_length=45),
            preserve_default=False,
        ),
    ]
