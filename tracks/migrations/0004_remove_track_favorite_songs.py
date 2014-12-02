# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0003_track_favorite_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='favorite_songs',
        ),
    ]
