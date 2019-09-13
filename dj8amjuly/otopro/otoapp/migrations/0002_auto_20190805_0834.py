# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='abc',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='otoapp.Student'),
        ),
    ]
