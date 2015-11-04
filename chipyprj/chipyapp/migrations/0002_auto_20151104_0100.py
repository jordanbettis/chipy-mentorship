# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.SmallIntegerField()),
                ('quarter', models.SmallIntegerField()),
                ('time', models.IntegerField()),
                ('active_unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', models.CharField(max_length=10)),
                ('hsd', models.CharField(max_length=10)),
                ('cdv', models.CharField(max_length=10)),
                ('xhs', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Penetration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.SmallIntegerField()),
                ('quarter', models.SmallIntegerField()),
                ('penetration', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='complex',
            name='unit',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='penetration',
            name='complex_code',
            field=models.ForeignKey(to='chipyapp.Complex'),
        ),
        migrations.AddField(
            model_name='penetration',
            name='data_type',
            field=models.ForeignKey(to='chipyapp.DataType'),
        ),
        migrations.AddField(
            model_name='activeunit',
            name='complex_code',
            field=models.ForeignKey(to='chipyapp.Complex'),
        ),
        migrations.AddField(
            model_name='activeunit',
            name='data_type',
            field=models.ForeignKey(to='chipyapp.DataType'),
        ),
    ]
