# Generated by Django 4.2.19 on 2025-03-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(blank=True, to='project.instructors', verbose_name='Инструктор'),
        ),
    ]
