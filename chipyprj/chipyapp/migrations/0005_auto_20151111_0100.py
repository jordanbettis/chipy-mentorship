# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipyapp', '0004_auto_20151110_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='LOB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lob', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='activeunit',
            name='time',
        ),
    ]
