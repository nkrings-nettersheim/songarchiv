# Generated by Django 3.0.7 on 2020-09-10 11:20

#import ckeditor.fields
from django_ckeditor_5.fields import CKEditor5Field
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songarchiv', '0022_song_song_activ'),
    ]

    operations = [
        migrations.CreateModel(
            name='content_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_kurz', models.CharField(default='', max_length=256)),
                ('content_lang', CKEditor5Field()),
            ],
        ),
    ]
