# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160813_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
