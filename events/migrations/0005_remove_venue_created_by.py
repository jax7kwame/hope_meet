# Generated by Django 5.0.4 on 2024-12-09 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_rename_image1_venue_image_remove_venue_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='created_by',
        ),
    ]
