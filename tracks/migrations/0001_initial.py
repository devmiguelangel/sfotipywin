# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=140)),
                ('order', models.PositiveIntegerField()),
                ('track_file', models.FileField(upload_to='track')),
                ('album', models.ForeignKey(to='albums.Album')),
                ('artist', models.ForeignKey(to='artists.Artist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
