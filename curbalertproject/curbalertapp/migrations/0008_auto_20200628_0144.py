# Generated by Django 3.0.7 on 2020-06-28 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curbalertapp', '0007_auto_20200628_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='expires_on',
            field=models.DateTimeField(),
        ),
    ]