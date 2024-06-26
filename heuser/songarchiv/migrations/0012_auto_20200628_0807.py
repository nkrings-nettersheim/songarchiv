# Generated by Django 3.0.7 on 2020-06-28 06:07

#import ckeditor.fields
from django_ckeditor_5.fields import CKEditor5Field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songarchiv', '0011_auto_20200621_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='song_text',
            name='text_chordpro',
            field=CKEditor5Field(default='Noch nicht befüllt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song_text',
            name='text_standard_german',
            field=CKEditor5Field(default='noch nicht befüllt'),
            preserve_default=False,
        ),
    ]
