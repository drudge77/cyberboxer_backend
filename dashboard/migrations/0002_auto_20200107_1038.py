# Generated by Django 3.0.1 on 2020-01-07 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='Latitude',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='Longitude',
            new_name='longitude',
        ),
    ]
