# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=100)),
                ('salesamt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('skid', models.AutoField(primary_key=True, serialize=False)),
                ('skname', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('skills_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='multipleapp.Skills')),
                ('emp_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='multipleapp.Emp')),
                ('customer_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='multipleapp.Customer')),
                ('sname', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
            ],
            bases=('multipleapp.customer', 'multipleapp.emp', 'multipleapp.skills'),
        ),
    ]
