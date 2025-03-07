from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории книг'
        verbose_name_plural = 'Категории книг'


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    author = models.CharField(max_length=100, verbose_name="Имя Автора")
    desc = models.TextField(verbose_name="Описание")
    Page_Count = models.CharField(max_length=100, verbose_name="Название", blank=True, null=True)
    Word_Count = models.CharField(max_length=100,    verbose_name="Название", blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'Книги'


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to='images/', verbose_name="Фото")
    price = models.DecimalField(verbose_name="цена", decimal_places=2, max_digits=8)
    count_lections = models.CharField(
        help_text="12 лекции", max_length=100, verbose_name="Количество лекции")
    hours = models.CharField(verbose_name="Сколько часов", max_length=20)
    description = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'


class SocialLinks(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название соцсети")
    link = models.CharField(max_length=255, verbose_name="ссылка")
    image = models.CharField(max_length=255, verbose_name="ссылка на лого")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Соц.сеть'
        verbose_name_plural = 'Соц.сеть'

class Instructors(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя фамилие")
    image = models.ImageField(upload_to='images/', verbose_name="Фото ава")
    position = models.CharField(max_length=100, verbose_name="Должность")
    description = RichTextField()

    def __str__(self):
        return f"{self.name} - {self.position}"

    class Meta:
        verbose_name = 'Инструкторы'
        verbose_name_plural = 'Инструкторы'


class Reviews(models.Model):
    name = models.CharField(max_length=100, verbose_name="фио")
    desc = models.TextField(verbose_name="Описание")
    rating = models.IntegerField(default=1, verbose_name="Рейтинг")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'