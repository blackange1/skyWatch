# Generated by Django 5.1.4 on 2024-12-08 22:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0006_remove_radardata_is_left_radar_is_left'),
    ]

    operations = [
        migrations.AddField(
            model_name='radardata',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
