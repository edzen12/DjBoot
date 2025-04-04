from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    gender_choices = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.username


class Settings(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название сайта")
    logo = models.ImageField(upload_to='images', verbose_name="Лого")
    phone1 = models.CharField(
        max_length=20, verbose_name="Телефон",
        help_text="Вы можете начать номер телефона с +996 (700) 700 700")
    phone2 = models.CharField(
        null=True, max_length=20, verbose_name="Телефон", blank=True,
        help_text="Вы можете начать номер телефона с +996 (500) 700 700")
    email = models.CharField(max_length=100, verbose_name="E-mail")
    email2 = models.CharField(max_length=100, verbose_name="E-mail", blank=True, null=True,)
    address = models.CharField(max_length=255, verbose_name="Адрес",null=True)
    map = models.TextField(verbose_name="карта", null=True)

    def __str__(self):
        return f"{self.name} {self.phone1}"

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категории книг'
        verbose_name_plural = 'Категории книг'


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    author = models.CharField(max_length=100, verbose_name="Имя Автора")
    image = models.CharField(max_length=255, verbose_name="Фото", help_text='вставьте ссылку', blank=True, null=True)
    desc = models.TextField(verbose_name="Описание")
    Page_Count = models.CharField(max_length=100, verbose_name="количество страниц", blank=True, null=True)
    Word_Count = models.CharField(max_length=100,    verbose_name="год", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'Книги'


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to='images/', verbose_name="Фото")
    price = models.DecimalField(verbose_name="цена", decimal_places=2, max_digits=8)
    instructors = models.ManyToManyField(
        'Instructors', blank=True, verbose_name="Инструктор")
    count_lections = models.CharField(
        help_text="12 лекции", max_length=100, verbose_name="Количество лекции")
    hours = models.CharField(verbose_name="Сколько часов", max_length=20)
    description = CKEditor5Field()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'


class SocialLinks(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название соцсети")
    instructor = models.ForeignKey(
        'Instructors', models.CASCADE, related_name='social_links', 
        null=True, blank=True)
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
    description = CKEditor5Field()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.position}"
    
    def get_absolute_url(self):
        return reverse("instructors_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Инструкторы'
        verbose_name_plural = 'Инструкторы'


class Reviews(models.Model):# Отзывы
    blog = models.ForeignKey(
        'Blog', on_delete=models.CASCADE, 
        related_name='reviews', verbose_name="Блог", null=True, blank=True
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='reviews', verbose_name="Блог",
        null=True, blank=True
    )
    name = models.CharField(max_length=100, verbose_name="фио")
    email = models.EmailField(verbose_name="Email", null=True)
    desc = models.TextField(verbose_name="Описание")
    rating = models.IntegerField(
        default=1, verbose_name="Рейтинг",
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания", null=True)

    def __str__(self):
        return f"{self.name} - ответ на {self.parent.name}" if self.parent else f"{self.name}"

    def get_replies(self):
        return self.replies.all()

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to='images/', verbose_name="Фото")   
    description = CKEditor5Field()
    author = models.CharField(verbose_name="Автор", max_length=100)
    date_post = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

