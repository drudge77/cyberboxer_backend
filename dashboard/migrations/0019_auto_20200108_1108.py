# Generated by Django 3.0.1 on 2020-01-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20200108_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationcounty',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='organisationzipcode',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]