# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0004_auto_20141209_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='job_title',
            field=models.CharField(max_length=225, null=True, blank=True),
            preserve_default=True,
        ),
    ]
