# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0006_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='surname',
            name='side',
            field=models.BooleanField(default=b'D', choices=[(b'D', '\u043f\u043e-\u0431\u0430\u0442\u044c\u043a\u0443'), (b'M', '\u043f\u043e-\u043c\u0430\u043c\u0456')]),
        ),
    ]
