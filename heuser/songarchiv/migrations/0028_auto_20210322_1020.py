# Generated by Django 3.0.7 on 2021-03-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songarchiv', '0027_auto_20210321_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_snippet',
            field=models.FileField(blank=True, upload_to='mp3/'),
        ),
    ]
