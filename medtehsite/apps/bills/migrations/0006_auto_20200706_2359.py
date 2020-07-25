﻿# Generated by Django 2.2.4 on 2020-07-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0005_auto_20200706_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='supply',
            field=models.CharField(choices=[('Да', 'Получили'), ('Нет', 'Ожидаем')], default='Нет', max_length=5, verbose_name='Состояние поставки заказа'),
        ),
    ]
