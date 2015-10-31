# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128, null=True, blank=True)),
                ('gender', models.CharField(max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=1024)),
                ('area', models.CharField(max_length=512)),
                ('pin', models.IntegerField(default=0)),
                ('telephone', models.BigIntegerField(null=True, blank=True)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('type_of_complaint', models.CharField(default=b'OT', max_length=2, choices=[(b'CA', b'civic_amenities'), (b'ED', b'education'), (b'EN', b'environment'), (b'HO', b'hospital'), (b'JA', b'jail'), (b'OT', b'others'), (b'PO', b'police'), (b'SE', b'service')])),
                ('complaint_title', models.CharField(max_length=200)),
                ('complaint_desc', models.TextField()),
                ('solved', models.CharField(default=b'UNS', max_length=3, choices=[(b'SOL', b'solved'), (b'UNS', b'unsolved')])),
                ('preference', models.IntegerField(default=0, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
