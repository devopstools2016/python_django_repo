# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otoapp', '0003_auto_20190805_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='abc',
            field=models.OneToOneField(null=True, on_delete=models.SET(3), to='otoapp.Student'),
        ),
    ]
