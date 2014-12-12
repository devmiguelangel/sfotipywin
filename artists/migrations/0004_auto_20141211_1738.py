# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_artist_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='artist',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
