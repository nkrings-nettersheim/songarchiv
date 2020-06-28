# Generated by Django 3.0.7 on 2020-06-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songarchiv', '0003_auto_20200607_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=250)),
                ('album_year', models.DateField(default='1900-01-01')),
            ],
        ),
    ]
