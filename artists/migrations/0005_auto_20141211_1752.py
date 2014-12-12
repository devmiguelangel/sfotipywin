# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_auto_20141211_1738'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='artist',
            unique_together=set([]),
        ),
    ]
