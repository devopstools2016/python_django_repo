# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sname', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('proxyapp.student',),
        ),
    ]
