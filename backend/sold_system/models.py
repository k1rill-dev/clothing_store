from django.db import models

from authentication.models import User
from clothing_store.models import FurCoat, Hat, Bag, Gloves


class FurCoatSale(models.Model):
    date_sell: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")
    basket = models.ManyToManyField(FurCoat, verbose_name="Товары")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Продавец")
    count = models.PositiveIntegerField(default=0, verbose_name="Количество проданных шуб")

    def __str__(self):
        return str(self.date_sell)

    class Meta:
        managed = True
        verbose_name = "Продажа шуб"
        verbose_name_plural = "Продажи шуб"


class GlovesSale(models.Model):
    date_sell: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")
    basket = models.ManyToManyField(Gloves, verbose_name="Товары")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Продавец")
    count = models.PositiveIntegerField(default=0, verbose_name="Количество проданных перчаток")

    def __str__(self):
        return str(self.date_sell)

    class Meta:
        managed = True
        verbose_name = "Продажа перчаток"
        verbose_name_plural = "Продажи перчаток"


class BagSale(models.Model):
    date_sell: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")
    basket = models.ManyToManyField(Bag, verbose_name="Товары")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Продавец")
    count = models.PositiveIntegerField(default=0, verbose_name="Количество проданных сумок")

    def __str__(self):
        return str(self.date_sell)

    class Meta:
        managed = True
        verbose_name = "Продажа сумок"
        verbose_name_plural = "Продажи сумок"


class HatSale(models.Model):
    date_sell: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")
    basket = models.ManyToManyField(Hat, verbose_name="Товары")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Продавец")
    count = models.PositiveIntegerField(default=0, verbose_name="Количество проданных шапок")

    def __str__(self):
        return str(self.date_sell)

    class Meta:
        managed = True
        verbose_name = "Продажа шапок"
        verbose_name_plural = "Продажи шапок"
