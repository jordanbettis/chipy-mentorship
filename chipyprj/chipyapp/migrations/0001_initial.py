# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complex_name', models.CharField(max_length=500, blank=True)),
                ('complex_code', models.CharField(max_length=6)),
                ('hmc', models.CharField(max_length=4, blank=True)),
                ('area', models.ForeignKey(to='chipyapp.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('module_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='complex',
            name='module',
            field=models.ForeignKey(to='chipyapp.Module'),
        ),
    ]
