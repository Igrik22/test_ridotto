# Generated by Django 3.2.9 on 2021-11-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_buyers', models.IntegerField(verbose_name='количество покупателей')),
                ('number_of_purchases', models.IntegerField(verbose_name='количество покупок')),
                ('total_amount', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='общая сумма покупок')),
            ],
        ),
    ]
