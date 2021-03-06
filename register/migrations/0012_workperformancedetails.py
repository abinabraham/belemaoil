# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-18 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20190218_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPerformanceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_exectn_date', models.DateField()),
                ('location', models.CharField(max_length=75)),
                ('total_value_contract', models.IntegerField()),
                ('client_contact_person', models.CharField(max_length=45)),
                ('job_compltn_certificate', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
    ]
