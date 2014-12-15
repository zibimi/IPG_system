# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='category',
            field=models.ForeignKey(blank=True, to='recruit.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='client',
            field=models.ForeignKey(blank=True, to='recruit.Client', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='emp_type',
            field=models.ForeignKey(blank=True, to='recruit.EmpType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='hours',
            field=models.ForeignKey(blank=True, to='recruit.Hours', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='keywords',
            field=models.ManyToManyField(to='recruit.Skill', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='priority',
            field=models.ForeignKey(blank=True, to='recruit.Priority', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='recruiter',
            field=models.ForeignKey(blank=True, to='recruit.Party', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='req_status',
            field=models.ForeignKey(to='recruit.ReqStatus'),
            preserve_default=True,
        ),
    ]
