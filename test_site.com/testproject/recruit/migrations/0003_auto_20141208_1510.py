# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0002_auto_20141121_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client'},
        ),
        migrations.AlterModelOptions(
            name='emptype',
            options={'verbose_name': 'EmpType'},
        ),
        migrations.AlterModelOptions(
            name='hours',
            options={'verbose_name': 'Hours'},
        ),
        migrations.AlterModelOptions(
            name='party',
            options={'verbose_name': 'Party'},
        ),
        migrations.AlterModelOptions(
            name='party_skill',
            options={'verbose_name': 'Party_Skill'},
        ),
        migrations.AlterModelOptions(
            name='priority',
            options={'verbose_name': 'Priority'},
        ),
        migrations.AlterModelOptions(
            name='reqstatus',
            options={'verbose_name': 'ReqStatus'},
        ),
        migrations.AlterModelOptions(
            name='requisition',
            options={'verbose_name': 'Requisition'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Skill'},
        ),
        migrations.AlterModelOptions(
            name='submittal',
            options={'verbose_name': 'Submittal'},
        ),
        migrations.AlterModelOptions(
            name='timesheet',
            options={'verbose_name': 'TimeSheet'},
        ),
    ]
