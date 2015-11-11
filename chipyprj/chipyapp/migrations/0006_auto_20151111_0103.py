# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipyapp', '0005_auto_20151111_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeunit',
            name='data_type',
        ),
        migrations.RemoveField(
            model_name='penetration',
            name='data_type',
        ),
        migrations.AddField(
            model_name='activeunit',
            name='lob',
            field=models.ForeignKey(default=0, to='chipyapp.LOB'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='penetration',
            name='lob',
            field=models.ForeignKey(default=0, to='chipyapp.LOB'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DataType',
        ),
    ]
