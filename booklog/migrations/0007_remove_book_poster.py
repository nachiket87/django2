# Generated by Django 3.0.2 on 2020-05-03 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklog', '0006_book_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='poster',
        ),
    ]
