# Generated by Django 5.0.4 on 2024-12-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_remove_event_latitude_remove_event_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_virtual',
            field=models.BooleanField(default=False),
        ),
    ]
