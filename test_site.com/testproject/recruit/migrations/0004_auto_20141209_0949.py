# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0003_auto_20141208_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Client'},
        ),
        migrations.AlterModelOptions(
            name='emptype',
            options={'verbose_name': 'EmpType', 'verbose_name_plural': 'EmpType'},
        ),
        migrations.AlterModelOptions(
            name='hours',
            options={'verbose_name': 'Hours', 'verbose_name_plural': 'Hours'},
        ),
        migrations.AlterModelOptions(
            name='party',
            options={'verbose_name': 'Party', 'verbose_name_plural': 'Party'},
        ),
        migrations.AlterModelOptions(
            name='party_skill',
            options={'verbose_name': 'Party_Skill', 'verbose_name_plural': 'Party_Skill'},
        ),
        migrations.AlterModelOptions(
            name='priority',
            options={'verbose_name': 'Priority', 'verbose_name_plural': 'Priority'},
        ),
        migrations.AlterModelOptions(
            name='reqstatus',
            options={'verbose_name': 'ReqStatus', 'verbose_name_plural': 'ReqStatus'},
        ),
        migrations.AlterModelOptions(
            name='requisition',
            options={'verbose_name': 'Requisition', 'verbose_name_plural': 'Requisition'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skill'},
        ),
        migrations.AlterModelOptions(
            name='submittal',
            options={'verbose_name': 'Submittal', 'verbose_name_plural': 'Submittal'},
        ),
        migrations.AlterModelOptions(
            name='timesheet',
            options={'verbose_name': 'TimeSheet', 'verbose_name_plural': 'TimeSheet'},
        ),
        migrations.AlterField(
            model_name='party',
            name='address',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='city',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='email',
            field=models.EmailField(max_length=75, verbose_name=b'e-mail', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='linkedin',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='phone',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='portfolio_link',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='resume_link',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='source',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='state',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='visa_status',
            field=models.CharField(max_length=45, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='zip',
            field=models.IntegerField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
