# Generated by Django 3.0.7 on 2020-06-28 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curbalertapp', '0012_auto_20200628_0547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='deleted',
        ),
    ]
