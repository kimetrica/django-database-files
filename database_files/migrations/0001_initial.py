# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone

from south.db import db
from south.v2 import SchemaMigration

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, db_index=True)),
                ('size', models.PositiveIntegerField(db_index=True)),
                ('content', models.BinaryField()),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created datetime', db_index=True)),
                ('_content_hash', models.CharField(db_index=True, max_length=128, null=True, db_column='content_hash', blank=True)),
            ],
            options={
                'db_table': 'database_files_file',
            },
        ),
    ]
