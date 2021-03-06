# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-20 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0024_auto_20190218_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCodeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_country', models.CharField(blank=True, max_length=200, null=True)),
                ('country_code', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_file', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
        migrations.AddField(
            model_name='registrationmodel',
            name='country_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='register.CountryCodeMaster'),
        ),
    ]
