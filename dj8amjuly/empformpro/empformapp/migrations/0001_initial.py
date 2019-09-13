# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ename', models.CharField(max_length=100)),
                ('sal', models.IntegerField()),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
