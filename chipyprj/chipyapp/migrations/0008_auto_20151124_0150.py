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
                ('property_type', models.CharField(max_length=10)),
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
            field=models.ForeignKey(default=0, to='chipyapp.PropertyType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complex',
            name='service_status',
            field=models.ForeignKey(default=0, to='chipyapp.ServiceStatus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complex',
            name='team',
            field=models.ForeignKey(default=1, to='chipyapp.Team'),
            preserve_default=False,
        ),
    ]
