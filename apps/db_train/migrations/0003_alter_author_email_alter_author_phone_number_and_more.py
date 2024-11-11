# Generated by Django 4.2.5 on 2024-10-09 16:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0002_alter_author_options_alter_author_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(help_text='Адрес почты в формате *@*.*', max_length=254, unique=True, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='author',
            name='phone_number',
            field=models.CharField(blank=True, help_text="Введите номер телефона через '+7' без пробелов в формате +79123456789 ", max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Телефонный номер должен быть формата: '+79123456789'.", regex='^\\+79\\d{9}$')], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.SlugField(help_text="Введите username, не длиннее 50 символов. Использовать нужно английский алфавит, разделять фразы нужно символом '-'", unique=True, verbose_name='Имя аккаунта'),
        ),
    ]