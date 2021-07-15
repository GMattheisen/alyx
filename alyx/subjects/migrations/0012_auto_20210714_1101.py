# Generated by Django 3.0.7 on 2021-07-14 11:01

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0011_auto_20210428_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subproject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(blank=True, help_text='Description of the subproject', max_length=1023)),
                ('users', models.ManyToManyField(blank=True, help_text='Persons associated to the subproject.', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='subprojects',
            field=models.ManyToManyField(blank=True, help_text='Subproject associated to this session', to='subjects.Subproject', verbose_name='Subject Subprojects'),
        ),
    ]