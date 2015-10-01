# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0008_auto_20151001_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surname',
            name='side',
            field=models.CharField(default='\u043f\u043e-\u0431\u0430\u0442\u044c\u043a\u0443', max_length=9, choices=[('\u043f\u043e-\u0431\u0430\u0442\u044c\u043a\u0443', '\u043f\u043e-\u0431\u0430\u0442\u044c\u043a\u0443'), ('\u043f\u043e-\u043c\u0430\u043c\u0456', '\u043f\u043e-\u043c\u0430\u043c\u0456')]),
        ),
    ]
