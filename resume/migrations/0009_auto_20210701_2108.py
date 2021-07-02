# Generated by Django 3.2.4 on 2021-07-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20210630_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myprojects',
            old_name='project_url',
            new_name='project_code_url',
        ),
        migrations.AddField(
            model_name='myprojects',
            name='project_live_url',
            field=models.URLField(blank=True, verbose_name='Link to live page'),
        ),
    ]
