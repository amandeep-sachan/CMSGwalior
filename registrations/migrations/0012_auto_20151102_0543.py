# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0011_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='telephone',
            field=models.BigIntegerField(default=0, null=True, blank=True),
        ),
    ]
