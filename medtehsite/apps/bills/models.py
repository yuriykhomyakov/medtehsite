﻿from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Bill(models.Model):

    BOOL = {
        ('Да', 'Получили'),
        ('Нет', 'Ожидаем'),
    }

    product = models.CharField(max_length=200,          # Запчасть. Краткое название запчасти (товара, услуги и т.д.)
                               verbose_name='Название запчасти')
    supplier = models.CharField(max_length=50,          # Поставщик. Краткое название организации у которой заказали
                                verbose_name='Поставщик')
    clinic = models.CharField(max_length=50,            # Больница. Для ремонта в которой нужна з/часть
                              verbose_name='ЛПУ')
    device = models.CharField(max_length=100,           # Аппарат на который пойдут запчасти
                              blank=True,
                              verbose_name='Аппарат')
    engineer = models.CharField(max_length=50,          # Техник (инженер), которому нужно отдать запчасть.
                                verbose_name='Техник')
    # -------------------------
    supply = models.CharField(max_length=5,             # Состояние поставки. "Да" если заказ доставлен
                              choices=BOOL,
                              default='Нет',
                              verbose_name='Состояние поставки заказа')
    supply_date = models.DateField(blank=True,          # Дата доставки.
                                   null=True,
                                   verbose_name='Дата прихода заказа')
    order_date = models.DateField(auto_now_add=True,    # Дата создания заказа (передачи в оплату)
                                  verbose_name='Дата создания заказа')
    order_author = models.ForeignKey(User,
                                     on_delete=models.SET_NULL,
                                     blank=True,
                                     null=True)
    bill_number = models.CharField(max_length=50,       # Номер счёта. Не обязательное
                                   blank=True,
                                   verbose_name='Номер счёта')
    bill_date = models.DateField(blank=True,            # Дата указанная в счете. Не обязательное
                                 null=True,
                                 verbose_name='Дата счёта')
    bill_sum = models.DecimalField(max_digits=9,        # Сумма в счёте. Не обязательная
                                   decimal_places=2,
                                   blank=True,
                                   null=True,
                                   verbose_name='Сумма в счёте')
    comment = models.TextField(blank=True,              # Комментарий к заказу
                               verbose_name='Комментарий')

    def delivered(self):
        self.supply_date = datetime.now().date()
        self.supply = 'Да'
        self.save()

    def __str__(self):
        return str(self.pk) + ' ' + str(self.product) + ' для ' + str(self.clinic)

    # Функция расчёта дней прошедших от заказа до получения (или до текущего дня, если заказ ещё не получен)
    @property
    def days_count(self):
        if self.supply == 'Да':
            supply_day = self.supply_date
        else:
            supply_day = datetime.now().date()
        return (supply_day - self.order_date).days

    class Meta:

        ordering = ['pk']

        verbose_name = 'Заказ по счёту'
        verbose_name_plural = 'Заказы по счёту'

