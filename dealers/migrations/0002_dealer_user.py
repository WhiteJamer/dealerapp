# Generated by Django 3.0 on 2019-12-12 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dealers', to=settings.AUTH_USER_MODEL),
        ),
    ]
