# Generated by Django 3.0 on 2019-12-12 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uprofile', '0006_auto_20191128_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]
