# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipyapp', '0006_auto_20151111_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeunit',
            name='quarter',
            field=models.SmallIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='activeunit',
            name='year',
            field=models.SmallIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='penetration',
            name='quarter',
            field=models.SmallIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='penetration',
            name='year',
            field=models.SmallIntegerField(db_index=True),
        ),
    ]
