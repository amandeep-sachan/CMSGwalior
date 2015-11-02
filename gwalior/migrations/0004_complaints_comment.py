# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwalior', '0003_auto_20151101_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='comment',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
