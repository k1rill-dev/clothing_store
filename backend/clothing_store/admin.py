from typing import TypeVar, Generic

from django.contrib import admin

from .models import FurCoat, Gloves, Bag, Hat

admin.site.site_header = "Управление товарами"

Model = TypeVar("Model")


class GenericClothesAdmin(admin.ModelAdmin, Generic[Model]):
    list_display = ['product', 'season', 'brand']
    list_filter = ['product', 'brand']
    list_display_links = ['product']
    # inlines = []
    raw_id_fields = ['product']
    readonly_fields = ['product', 'season', 'brand']
    search_fields = ['product', 'season', 'brand']
    ordering = ['product__date_of_receipt']


@admin.register(FurCoat)
class FurCoatAdmin(GenericClothesAdmin[FurCoat]):
    pass


@admin.register(Gloves)
class GlovesAdmin(GenericClothesAdmin[Gloves]):
    pass


@admin.register(Bag)
class BagAdmin(GenericClothesAdmin[Bag]):
    pass


@admin.register(Hat)
class HatAdmin(GenericClothesAdmin[Hat]):
    pass
