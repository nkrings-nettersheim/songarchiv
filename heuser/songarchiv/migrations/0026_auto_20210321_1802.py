# Generated by Django 3.0.7 on 2021-03-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songarchiv', '0025_auto_20210320_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
        migrations.AddField(
            model_name='song',
            name='song_cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
    ]
