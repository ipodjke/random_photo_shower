# Generated by Django 4.2.4 on 2023-08-10 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_contents', '0002_alter_photo_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
