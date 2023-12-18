import uuid
from django.db import models


class Material(models.Model):
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="UUID"
    )
    title: models.CharField = models.CharField(max_length=255, verbose_name="Материал")

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Brand(models.Model):
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="UUID"
    )
    brand: models.CharField = models.CharField(max_length=255, verbose_name="Бренд")

    def __str__(self):
        return self.brand

    class Meta:
        managed = True
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class ManufacturerCountry(models.Model):
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="UUID"
    )
    manufacturer: models.CharField = models.CharField(max_length=255, verbose_name="Бренд")

    def __str__(self):
        return self.manufacturer

    class Meta:
        managed = True
        verbose_name = 'Страна-производитель'
        verbose_name_plural = 'Страны-производителя'


class Season(models.Model):
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="UUID"
    )
    season: models.CharField = models.CharField(max_length=255, verbose_name="Сезон")

    def __str__(self):
        return self.season

    class Meta:
        managed = True
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'


class Size(models.Model):
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="UUID"
    )
    size: models.CharField = models.CharField(max_length=255, verbose_name="Размер")

    def __str__(self):
        return self.size

    class Meta:
        managed = True
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Product(models.Model):
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="UUID"
    )
    title: models.CharField = models.CharField(max_length=255, verbose_name="Название")
    color: models.CharField = models.CharField(max_length=255, verbose_name="Цвет")
    description: models.CharField = models.CharField(max_length=255, verbose_name="Описание")
    sizes: models.ManyToManyField = models.ManyToManyField(Size, null=True, blank=True, verbose_name="Размеры")
    date_of_receipt: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="Дата завоза")

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class AbstractProduct(models.Model):
    price: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name="Цена", default=0)
    product: Product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Инфо о товаре")
    season: Season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name="Сезон")
    brand: Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд")
    manufacturer: ManufacturerCountry = models.ForeignKey(ManufacturerCountry, on_delete=models.CASCADE,
                                                          verbose_name="Производитель")
    material: Material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Материал")

    def __str__(self):
        return self.product.name

    class Meta:
        abstract = True


class FurCoat(AbstractProduct):
    id: models.UUIDField = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="UUID"
    )
    removable_part: models.CharField = models.CharField(max_length=255, verbose_name="Съемная часть")
    hood: models.CharField = models.CharField(max_length=255, verbose_name="Капюшон")
    clasp: models.CharField = models.CharField(max_length=255, verbose_name="Застежки")
    length: models.IntegerField = models.IntegerField(verbose_name="Длина")
    shadow: models.CharField = models.CharField(max_length=255, verbose_name="Силуэт")
    collar_style: models.CharField = models.CharField(max_length=255, verbose_name="Стиль воротника")

    class Meta:
        managed = True
        verbose_name = 'Шуба'
        verbose_name_plural = 'Шубы'


class Gloves(AbstractProduct):
    class Meta:
        managed = True
        verbose_name = 'Перчатки'
        verbose_name_plural = 'Перчатки'


class Hat(AbstractProduct):
    class Meta:
        managed = True
        verbose_name = 'Шапка'
        verbose_name_plural = 'Шапки'


class Bag(AbstractProduct):
    clasp: models.CharField = models.CharField(max_length=255, verbose_name="Застежки")
    width: models.FloatField = models.FloatField(verbose_name="Ширина")
    width_of_bottom: models.FloatField = models.FloatField(verbose_name="Ширина дна")
    height: models.FloatField = models.FloatField(verbose_name="Высота")
    belt: models.CharField = models.CharField(max_length=255, verbose_name="Ремень")
    equipment: models.CharField = models.CharField(max_length=255, verbose_name="Комплектация")
    legs: models.CharField = models.CharField(max_length=255, verbose_name="Ножки")
    inside_pockets_count: models.IntegerField = models.IntegerField(verbose_name="Кол-во внутренних карманов")

    class Meta:
        managed = True
        verbose_name = 'Сумка'
        verbose_name_plural = 'Сумки'
