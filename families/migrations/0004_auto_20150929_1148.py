# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0003_auto_20150929_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relative',
            name='father',
            field=models.OneToOneField(related_name='child_dad', null=True, blank=True, to='families.Relative'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='mother',
            field=models.OneToOneField(related_name='child_mom', null=True, blank=True, to='families.Relative'),
        ),
    ]
