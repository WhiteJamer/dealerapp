# Generated by Django 2.2.7 on 2019-11-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uprofile', '0005_auto_20191121_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
