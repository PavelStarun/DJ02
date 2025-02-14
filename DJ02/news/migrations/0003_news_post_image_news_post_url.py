# Generated by Django 5.0.7 on 2024-07-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_newspost_news_post_alter_news_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='news_post',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
    ]
