# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipyapp', '0007_auto_20151111_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='complex',
            name='property_type',
            field=models.ForeignKey(blank=True, to='chipyapp.PropertyType', null=True),
        ),
        migrations.AddField(
            model_name='complex',
            name='service_status',
            field=models.ForeignKey(blank=True, to='chipyapp.ServiceStatus', null=True),
        ),
        migrations.AddField(
            model_name='complex',
            name='team',
            field=models.ForeignKey(blank=True, to='chipyapp.Team', null=True),
        ),
    ]
