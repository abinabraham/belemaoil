# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-07 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20190307_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='AviationSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='majorcategory',
            name='aviation',
            field=models.ManyToManyField(blank=True, null=True, to='services.AviationSupport'),
        ),
    ]
