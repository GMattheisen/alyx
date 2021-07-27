# Generated by Django 3.0.7 on 2021-07-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0012_auto_20210714_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subprojects',
            field=models.ManyToManyField(blank=True, help_text='Subproject associated to this session', null=True, to='subjects.Subproject', verbose_name='Subject Subprojects'),
        ),
    ]