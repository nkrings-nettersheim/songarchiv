# Generated by Django 3.0.7 on 2020-06-07 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songarchiv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='song_titel',
            new_name='song_title',
        ),
    ]
