# Generated by Django 3.0.1 on 2020-01-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200107_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='last_update',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
