# Generated by Django 3.0.7 on 2020-06-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curbalertapp', '0004_auto_20200627_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='expires_on',
            field=models.DateField(),
        ),
    ]
