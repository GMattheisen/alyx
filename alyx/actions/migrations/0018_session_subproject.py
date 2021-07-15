# Generated by Django 3.0.7 on 2021-07-14 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0012_auto_20210714_1101'),
        ('actions', '0017_auto_20210430_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='subproject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Subproject', verbose_name='Session Subproject'),
        ),
    ]
