from typing import Generic, TypeVar

from django.db import models

from clothing_store.models import FurCoat, Hat, Bag, Gloves


class FurCoatSale(models.Model):
    date_sell: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")
    basket = models.ManyToManyField(FurCoat, verbose_name="Товары")

    def __str__(self):
        return str(self.date_sell)

    class Meta:
        managed = True
        verbose_name = "Продажа шуб"
        verbose_name_plural = "Продажи шуб"


class GlovesSale(models.Model):
    date_sell: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")
    basket = models.ManyToManyField(Gloves, verbose_name="Товары")

    def __str__(self):
        return str(self.date_sell)

    class Meta:
        managed = True
        verbose_name = "Продажа перчаток"
        verbose_name_plural = "Продажи перчаток"



class BagSale(models.Model):
    date_sell: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")
    basket = models.ManyToManyField(Bag, verbose_name="Товары")

    def __str__(self):
        return str(self.date_sell)

    class Meta:
        managed = True
        verbose_name = "Продажа сумок"
        verbose_name_plural = "Продажи сумок"



class HatSale(models.Model):
    date_sell: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")
    basket = models.ManyToManyField(Hat, verbose_name="Товары")

    def __str__(self):
        return str(self.date_sell)

    class Meta:
        managed = True
        verbose_name = "Продажа шапок"
        verbose_name_plural = "Продажи шапок"
