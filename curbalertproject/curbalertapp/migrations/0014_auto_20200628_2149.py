# Generated by Django 3.0.7 on 2020-06-28 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curbalertapp', '0013_remove_donation_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerter',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]
