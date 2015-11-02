# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwalior', '0004_complaints_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='telephone',
            field=models.BigIntegerField(default=b'0', null=True, blank=True),
        ),
    ]
