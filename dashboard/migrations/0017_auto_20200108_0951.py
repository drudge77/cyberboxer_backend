# Generated by Django 3.0.1 on 2020-01-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_organisationzipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationcounty',
            name='orgs_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
