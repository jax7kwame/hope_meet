# Generated by Django 5.0.4 on 2024-12-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_event_latitude_event_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='event',
            name='longitude',
        ),
        migrations.AddField(
            model_name='venue',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]