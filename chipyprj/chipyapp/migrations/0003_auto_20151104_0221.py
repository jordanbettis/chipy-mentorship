# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipyapp', '0002_auto_20151104_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complex',
            name='complex_code',
            field=models.CharField(max_length=10),
        ),
    ]
