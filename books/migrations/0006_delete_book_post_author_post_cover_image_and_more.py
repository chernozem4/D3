# Generated by Django 5.1.1 on 2024-09-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_remove_post_created_at_remove_post_description_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=255, null=True, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='books/', verbose_name='Обложка книги'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('fiction', 'Fiction'), ('nonfiction', 'Non-fiction'), ('fantasy', 'Fantasy'), ('science_fiction', 'Science Fiction'), ('mystery', 'Mystery'), ('biography', 'Biography')], max_length=50, null=True, verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='post',
            name='like_or_dislike',
            field=models.CharField(blank=True, choices=[('👍🏻', '👍🏻'), ('👎🏻', '👎🏻')], max_length=100, null=True, verbose_name='Нравится или нет'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Название книги'),
        ),
    ]
