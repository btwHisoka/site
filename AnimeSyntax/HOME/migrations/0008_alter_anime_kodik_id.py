# Generated by Django 5.1.4 on 2025-01-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0007_remove_anime_video_url_anime_kodik_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='kodik_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]
