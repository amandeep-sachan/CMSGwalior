# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=1024)),
                ('area', models.CharField(max_length=512)),
                ('pin', models.IntegerField(default=0)),
                ('telephone', models.BigIntegerField(null=True, blank=True)),
                ('mobile', models.BigIntegerField(unique=True)),
                ('education', models.CharField(default=b'NO', max_length=8, choices=[(b'GR', b'Graduation'), (b'PG', b'Post Graduation'), (b'VO', b'Vocational'), (b'HS', b'Higher Secondary'), (b'SE', b'Secondary'), (b'EL', b'Elementary'), (b'NO', b'None')])),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
