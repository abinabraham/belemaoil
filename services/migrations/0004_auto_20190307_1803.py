# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-07 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20190224_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstllMaintModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='consultancy',
            options={},
        ),
        migrations.AlterModelOptions(
            name='generalsupplies',
            options={},
        ),
        migrations.AlterModelOptions(
            name='heatingcoolingprod',
            options={},
        ),
        migrations.AlterModelOptions(
            name='laboratory',
            options={},
        ),
        migrations.AlterModelOptions(
            name='mechanicalparts',
            options={},
        ),
        migrations.AlterModelOptions(
            name='onshoreenv',
            options={},
        ),
        migrations.AlterModelOptions(
            name='protocollogistics',
            options={},
        ),
        migrations.AlterModelOptions(
            name='rehabcivil',
            options={},
        ),
        migrations.AlterModelOptions(
            name='rehabelectr',
            options={},
        ),
        migrations.AlterModelOptions(
            name='rehabmech',
            options={},
        ),
        migrations.AlterModelOptions(
            name='safetylabchem',
            options={},
        ),
        migrations.AlterModelOptions(
            name='waterborehole',
            options={},
        ),
        migrations.AddField(
            model_name='majorcategory',
            name='install',
            field=models.ManyToManyField(blank=True, null=True, to='services.InstllMaintModel'),
        ),
    ]
