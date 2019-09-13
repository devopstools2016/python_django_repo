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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cname', models.CharField(max_length=100)),
                ('salesamt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('customer_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='multilevelapp.Customer')),
                ('ename', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
            bases=('multilevelapp.customer',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('emp_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='multilevelapp.Emp')),
                ('sname', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
            ],
            bases=('multilevelapp.emp',),
        ),
    ]
