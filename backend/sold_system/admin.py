from typing import TypeVar, Generic

from django.contrib import admin

from sold_system.models import *


Model = TypeVar("Model", bound=models.Model)

admin.site.register(FurCoatSale)
admin.site.register(BagSale)
admin.site.register(HatSale)
admin.site.register(GlovesSale)