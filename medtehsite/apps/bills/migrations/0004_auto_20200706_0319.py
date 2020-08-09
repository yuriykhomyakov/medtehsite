# Generated by Django 2.2.4 on 2020-07-05 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_auto_20200706_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='supply',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=5, verbose_name='Состояние поставки заказа'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='supply_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Дата прихода заказа'),
        ),
    ]