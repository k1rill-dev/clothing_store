from typing import TypeVar, Generic

from django.contrib import admin

from .models import FurCoat, Gloves, Bag, Hat, Product, Size, Season, ManufacturerCountry, Brand, Material, \
    PhotoFurCoat, PhotoGloves, PhotoHat, PhotoBag

admin.site.site_header = "Управление товарами"

Model = TypeVar("Model")


class GenericClothesAdmin(admin.ModelAdmin, Generic[Model]):
    list_display = ['product', 'season', 'brand']
    list_filter = ['product', 'brand']
    list_display_links = ['product']
    raw_id_fields = ['product']
    search_fields = ['product', 'season', 'brand']
    ordering = ['product__date_of_receipt']


class PhotoFurCoatInline(admin.StackedInline):
    model = PhotoFurCoat


class PhotoGlovesInline(admin.StackedInline):
    model = PhotoGloves


class PhotoHatInline(admin.StackedInline):
    model = PhotoHat


class PhotoBagInline(admin.StackedInline):
    model = PhotoBag


@admin.register(FurCoat)
class FurCoatAdmin(GenericClothesAdmin[FurCoat]):
    inlines = [PhotoFurCoatInline]


@admin.register(Gloves)
class GlovesAdmin(GenericClothesAdmin[Gloves]):
    inlines = [PhotoGlovesInline]


@admin.register(Bag)
class BagAdmin(GenericClothesAdmin[Bag]):
    inlines = [PhotoBagInline]


@admin.register(Hat)
class HatAdmin(GenericClothesAdmin[Hat]):
    inlines = [PhotoHatInline]


admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Season)
admin.site.register(ManufacturerCountry)
admin.site.register(Brand)
admin.site.register(Material)
