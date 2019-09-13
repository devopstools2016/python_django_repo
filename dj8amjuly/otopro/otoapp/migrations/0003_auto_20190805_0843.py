# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otoapp', '0002_auto_20190805_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='abc',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='otoapp.Student'),
        ),
    ]
