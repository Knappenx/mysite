# Generated by Django 3.2.4 on 2021-06-30 15:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_rename_myprojec_myprojects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprojects',
            name='project_desc',
            field=models.TextField(max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='myprojects',
            name='project_name',
            field=models.CharField(max_length=20, verbose_name='Project NAme'),
        ),
        migrations.AlterField(
            model_name='myprojects',
            name='project_photo',
            field=models.URLField(blank=True, verbose_name='Preview photo link'),
        ),
        migrations.AlterField(
            model_name='myprojects',
            name='project_techs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, verbose_name='Project Technologies'), size=None),
        ),
        migrations.AlterField(
            model_name='myprojects',
            name='project_url',
            field=models.URLField(blank=True, verbose_name='Link to project'),
        ),
    ]