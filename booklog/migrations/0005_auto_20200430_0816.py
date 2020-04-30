# Generated by Django 3.0.2 on 2020-04-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklog', '0004_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='book_profile'),
        ),
        migrations.AlterField(
            model_name='book',
            name='review',
            field=models.CharField(choices=[('Good', 'Good'), ('Bad', 'Bad'), ('Terrible', 'Terrible')], max_length=10),
        ),
    ]