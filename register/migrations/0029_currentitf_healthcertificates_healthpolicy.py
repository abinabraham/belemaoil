# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-23 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0028_nplapp_refletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentITF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citf', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
        migrations.CreateModel(
            name='HealthCertificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
        migrations.CreateModel(
            name='HealthPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
    ]
