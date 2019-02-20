# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-18 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_certificateincorporation_companyprofilefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormCO10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c010_file', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
        migrations.CreateModel(
            name='FormCO2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co2_file', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
        migrations.CreateModel(
            name='FormCO7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co7_file', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgnztn_chart_file', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
        migrations.CreateModel(
            name='PastProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pjt_file', models.FileField(upload_to='media/contrator/files')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.ContractorModel')),
            ],
        ),
    ]
