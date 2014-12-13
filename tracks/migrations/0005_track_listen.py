# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_remove_track_favorite_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='listen',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
