# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category', models.CharField(max_length=45)),
                ('category_desc', models.CharField(max_length=1024, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('client', models.CharField(max_length=45)),
                ('client_desc', models.CharField(max_length=1024, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmpType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('emp_type', models.CharField(max_length=45)),
                ('emp_type_desc', models.CharField(max_length=1024, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hours', models.CharField(max_length=45)),
                ('hours_desc', models.CharField(max_length=1024, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=45, null=True, blank=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=75, verbose_name=b'e-mail')),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=45)),
                ('zip', models.IntegerField(max_length=10)),
                ('visa_status', models.CharField(max_length=45)),
                ('portfolio_link', models.CharField(max_length=256)),
                ('linkedin', models.URLField()),
                ('source', models.CharField(max_length=256)),
                ('resume_link', models.URLField()),
                ('ts_update', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Party_Skill',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('skill_lvl', models.CharField(max_length=45, null=True, blank=True)),
                ('skill_start_date', models.DateField(null=True, blank=True)),
                ('skill_year', models.IntegerField(null=True, blank=True)),
                ('skill_notes', models.CharField(max_length=1024, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('priority', models.CharField(max_length=45)),
                ('priority_desc', models.CharField(max_length=1024, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReqStatus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('req_status', models.CharField(max_length=45)),
                ('req_status_desc', models.CharField(max_length=1024, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('req_date', models.DateField(null=True, blank=True)),
                ('job_id', models.CharField(max_length=45, null=True, blank=True)),
                ('job_title', models.CharField(max_length=45, null=True, blank=True)),
                ('loc', models.CharField(max_length=45, null=True, blank=True)),
                ('duration', models.CharField(max_length=45, null=True, blank=True)),
                ('rate', models.CharField(max_length=45, null=True, blank=True)),
                ('openings', models.IntegerField(null=True, blank=True)),
                ('job_description', models.TextField(max_length=20000, null=True, blank=True)),
                ('req_contact', models.CharField(max_length=45, null=True, blank=True)),
                ('req_contact_notes', models.TextField(max_length=20000, null=True, blank=True)),
                ('city', models.CharField(max_length=45, null=True, blank=True)),
                ('state', models.CharField(max_length=45, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('req_approved', models.DateField(null=True, blank=True)),
                ('category', models.ForeignKey(default=1, blank=True, to='recruit.Category', null=True)),
                ('client', models.ForeignKey(default=1, blank=True, to='recruit.Client', null=True)),
                ('emp_type', models.ForeignKey(default=1, blank=True, to='recruit.EmpType', null=True)),
                ('hours', models.ForeignKey(default=1, blank=True, to='recruit.Hours', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('skill_name', models.CharField(max_length=256)),
                ('skill_desc', models.CharField(max_length=1024, null=True, blank=True)),
                ('skill_catagory', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submittal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hourly_rate', models.CharField(max_length=45)),
                ('current_year_rate', models.CharField(max_length=45)),
                ('expected_year_rate', models.CharField(max_length=45)),
                ('interview_available', models.CharField(max_length=45)),
                ('start_available', models.CharField(max_length=45)),
                ('interview_feedback', models.TextField(max_length=1000)),
                ('status', models.CharField(max_length=45)),
                ('interview_date', models.DateField()),
                ('candidate', models.ForeignKey(related_name='candidate', to='recruit.Party')),
                ('job_id', models.ForeignKey(to='recruit.Requisition')),
                ('recruiter', models.ForeignKey(related_name='recruiter', to='recruit.Party')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.CharField(max_length=45)),
                ('account', models.CharField(max_length=45)),
                ('site', models.CharField(max_length=45)),
                ('week_end', models.DateField()),
                ('st_hrs', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('ot_hrs', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('dt_hrs', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('nb_hrs', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('other_hrs', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('notes', models.TextField(max_length=20000, null=True, blank=True)),
                ('consultant', models.ForeignKey(to='recruit.Party')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='requisition',
            name='keywords',
            field=models.ManyToManyField(default=1, to='recruit.Skill', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requisition',
            name='priority',
            field=models.ForeignKey(default=1, blank=True, to='recruit.Priority', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requisition',
            name='recruiter',
            field=models.ForeignKey(default=1, blank=True, to='recruit.Party', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requisition',
            name='req_status',
            field=models.ForeignKey(default=1, to='recruit.ReqStatus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party_skill',
            name='skill',
            field=models.ForeignKey(to='recruit.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='skills',
            field=models.ManyToManyField(to='recruit.Party_Skill', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
