# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('courses', multiselectfield.db.fields.MultiSelectField(max_length=200, choices=[('py', 'Python'), ('dj', 'Django'), ('java', 'Java'), ('ui', 'UI'), ('Fl', 'Flask')])),
                ('branches', multiselectfield.db.fields.MultiSelectField(max_length=200, choices=[('hyd', 'Hyderabad'), ('bang', 'Bangalore'), ('che', 'Chennai'), ('pune', 'Pune')])),
                ('shifts', multiselectfield.db.fields.MultiSelectField(max_length=200, choices=[('mrg', 'Morning Shift'), ('aftn', 'Afternoon Shift'), ('evng', 'Evening Shift'), ('ngt', 'Night Shift')])),
                ('gender', models.CharField(max_length=20)),
                ('start_date', models.DateField(max_length=100)),
            ],
        ),
    ]
