# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0005_auto_20150929_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435',
                'verbose_name_plural': '\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0430',
            },
        ),
    ]
