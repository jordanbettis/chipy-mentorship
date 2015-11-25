# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipyapp', '0008_auto_20151124_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complex',
            name='complex_name',
        ),
        migrations.RemoveField(
            model_name='complex',
            name='hmc',
        ),
    ]
