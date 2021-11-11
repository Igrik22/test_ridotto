from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='имя покупателя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия покупателя')

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


class ShopInfo(models.Model):
    customers = models.ManyToManyField(Customer, related_name='shopinfos', verbose_name='покупатели')
    title = models.CharField(max_length=30, verbose_name='имя товара')
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(max_digits=7, decimal_places=3, verbose_name='цена')
    purchase_date = models.DateField(verbose_name='дата покупки')
    purchase_time = models.TimeField(verbose_name='время покупки')

    def __repr__(self):
        return {self.title}

