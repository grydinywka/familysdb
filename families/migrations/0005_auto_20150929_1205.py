# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0004_auto_20150929_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relative',
            name='father',
            field=models.ForeignKey(related_name='children_dad', blank=True, to='families.Relative', null=True),
        ),
        migrations.AlterField(
            model_name='relative',
            name='mother',
            field=models.ForeignKey(related_name='children_mom', blank=True, to='families.Relative', null=True),
        ),
    ]
