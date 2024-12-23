# Generated by Django 5.0.4 on 2024-12-01 17:37

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('author', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='uploads/news')),
                ('intro', tinymce.models.HTMLField()),
                ('body', tinymce.models.HTMLField()),
                ('youtube_video', models.CharField(blank=True, max_length=255)),
                ('random_quote', models.TextField()),
                ('quote_author', models.CharField(max_length=255)),
                ('published', models.BooleanField()),
                ('featured', models.BooleanField()),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
