# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipyapp', '0003_auto_20151104_0221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datatype',
            old_name='cdv',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='datatype',
            name='hsd',
        ),
        migrations.RemoveField(
            model_name='datatype',
            name='video',
        ),
        migrations.RemoveField(
            model_name='datatype',
            name='xhs',
        ),
    ]
