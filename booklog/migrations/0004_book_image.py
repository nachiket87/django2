# Generated by Django 3.0.2 on 2020-04-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklog', '0003_remove_book_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='book_cover_pic'),
        ),
    ]