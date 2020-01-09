# Generated by Django 3.0.1 on 2020-01-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20200107_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='activities_num',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='employee_band_company',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='kompass_id',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='nature',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='us_state',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='zip',
        ),
        migrations.AddField(
            model_name='organisation',
            name='address',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='city_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='county_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='employee_band_at_company',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='k_id',
            field=models.CharField(default=None, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='zipcode',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]