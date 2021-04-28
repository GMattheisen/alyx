# Generated by Django 2.1.4 on 2019-01-24 10:25

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0003_auto_20190124_1025'),
        ('actions', '0004_auto_20181122_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Long name', max_length=255)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('send_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('notification_type', models.CharField(choices=[('responsible_user_change', 'responsible user has changed'), ('mouse_underweight', 'mouse is underweight'), ('mouse_water', 'water to give to mouse'), ('mouse_training', 'check training days')], max_length=32)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('no-send', 'do not send'), ('to-send', 'to send'), ('sent', 'sent')], default='to-send', max_length=16)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Subject')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationRule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Long name', max_length=255)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('notification_type', models.CharField(choices=[('responsible_user_change', 'responsible user has changed'), ('mouse_underweight', 'mouse is underweight'), ('mouse_water', 'water to give to mouse'), ('mouse_training', 'check training days')], max_length=32)),
                ('subjects_scope', models.CharField(choices=[('none', 'none'), ('all', 'all'), ('mine', 'mine'), ('lab', 'lab')], max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='surgery',
            name='outcome_type',
            field=models.CharField(blank=True, choices=[('a', 'Acute'), ('r', 'Recovery'), ('n', 'Non-recovery')], max_length=1),
        ),
        migrations.AlterUniqueTogether(
            name='notificationrule',
            unique_together={('user', 'notification_type')},
        ),
    ]
