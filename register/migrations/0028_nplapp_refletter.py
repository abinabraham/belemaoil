# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-23 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0027_workperformancedetails_client_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NPLApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npl', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
        migrations.CreateModel(
            name='RefLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_file', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
    ]
