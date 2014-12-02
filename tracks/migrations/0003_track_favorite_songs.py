# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('tracks', '0002_auto_20141201_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='favorite_songs',
            field=models.ManyToManyField(related_name='favorite_of', blank=True, to='artists.Artist'),
            preserve_default=True,
        ),
    ]
