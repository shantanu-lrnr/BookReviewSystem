# Generated by Django 5.1.4 on 2024-12-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_info',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
