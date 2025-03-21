# Generated by Django 4.2.19 on 2025-03-03 13:10

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категории книг',
                'verbose_name_plural': 'Категории книг',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='цена')),
                ('count_lections', models.CharField(help_text='12 лекции', max_length=100, verbose_name='Количество лекции')),
                ('hours', models.CharField(max_length=20, verbose_name='Сколько часов')),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Курсы',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя фамилие')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Фото ава')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Инструкторы',
                'verbose_name_plural': 'Инструкторы',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='фио')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('rating', models.IntegerField(default=1, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название соцсети')),
                ('link', models.CharField(max_length=255, verbose_name='ссылка')),
                ('image', models.CharField(max_length=255, verbose_name='ссылка на лого')),
            ],
            options={
                'verbose_name': 'Соц.сеть',
                'verbose_name_plural': 'Соц.сеть',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('author', models.CharField(max_length=100, verbose_name='Имя Автора')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('Page_Count', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('Word_Count', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
