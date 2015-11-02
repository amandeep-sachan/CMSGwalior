# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwalior', '0002_auto_20151024_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='solved',
            field=models.CharField(default=b'NOT SOLVED', max_length=50, choices=[(b'SOLVED', b'solved'), (b'NOT SOLVED', b'unsolved'), (b'UNDER CONSIDERATION', b'under consideration')]),
        ),
    ]
