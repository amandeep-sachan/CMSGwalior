# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwalior', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='solved',
            field=models.CharField(default=b'NOT SOLVED', max_length=3, choices=[(b'SOLVED', b'solved'), (b'NOT SOLVED', b'unsolved'), (b'UNDER CONSIDERATION', b'under consideration')]),
        ),
    ]
