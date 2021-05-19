# Generated by Django 3.0.7 on 2021-04-30 15:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0016_session_dset_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='dset_types',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]