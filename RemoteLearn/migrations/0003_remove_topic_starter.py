# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RemoteLearn', '0002_auto_20200411_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='starter',
        ),
    ]
