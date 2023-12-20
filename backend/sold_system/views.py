from typing import List, Tuple

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.request import Request
from django.db.models import Model

from authentication.models import User
from clothing_store.models import FurCoat, Gloves, Bag, Hat
from sold_system.models import FurCoatSale, HatSale, BagSale, GlovesSale
from sold_system.serializers import FurCoatSaleSerializer, HatSaleSerializer, BagSaleSerializer, GlovesSaleSerializer
import enum


class Products(enum.Enum):
    fur_coat: str = 'fur_coat'
    hat: str = 'hat'
    gloves: str = 'gloves'
    bag: str = 'bag'


class FurCoatSaleViewSet(viewsets.ModelViewSet):
    queryset = FurCoatSale.objects.all()
    serializer_class = FurCoatSaleSerializer


class HatSaleViewSet(viewsets.ModelViewSet):
    queryset = HatSale.objects.all()
    serializer_class = HatSaleSerializer


class BagSaleViewSet(viewsets.ModelViewSet):
    queryset = BagSale.objects.all()
    serializer_class = BagSaleSerializer


class GlovesSaleViewSet(viewsets.ModelViewSet):
    queryset = GlovesSale.objects.all()
    serializer_class = GlovesSaleSerializer


def _get_model_object(product: dict, product_model: Model) -> Model:
    product_id = product.get("id")
    product_object = get_object_or_404(product_model, pk=product_id)
    return product_object

def _get_product(products: List[dict], user: User) -> JsonResponse:
    fur_coats_object_list = list();hat_object_list = list();gloves_object_list = list();bag_object_list = list()
    json = []
    for product in products:
        match product.get("type"):
            case Products.fur_coat.value:
                fur_coat = _get_model_object(product, FurCoat)
                for size in fur_coat.product.sizesproduct_set.all(): size.count -= product.get("size")
                fur_coats_object_list.append(fur_coat)
            case Products.gloves.value:
                gloves = _get_model_object(product, Gloves)
                for size in gloves.product.sizesproduct_set.all(): size.count -= product.get("size")
                gloves_object_list.append(gloves)
            case Products.bag.value:
                bag = _get_model_object(product, Bag)
                for size in bag.product.sizesproduct_set.all(): size.count -= product.get("size")
                bag_object_list.append(bag)
            case Products.hat.value:
                hat = _get_model_object(product, Hat)
                for size in hat.product.sizesproduct_set.all(): size.count -= product.get("size")
                hat_object_list.append(hat)
    if fur_coats_object_list:
        fur_coat_sale = FurCoatSale.objects.create(seller=user)
        fur_coat_sale.basket.set(fur_coats_object_list)
        fur_coat_serializer = FurCoatSaleSerializer(fur_coat_sale)
        json.append(fur_coat_serializer.data)
    if hat_object_list:
        hat_sale = HatSale.objects.create(seller=user)
        hat_sale.basket.set(hat_object_list)
        hat_sale_serializer = HatSaleSerializer(hat_sale)
        json.append(hat_sale_serializer.data)
    if gloves_object_list:
        gloves_sale = GlovesSale.objects.create(seller=user)
        gloves_sale.basket.set(gloves_object_list)
        gloves_sale_serializer = GlovesSaleSerializer(gloves_sale)
        json.append(gloves_sale_serializer.data)
    if bag_object_list:
        bag_sale = BagSale.objects.create(seller=user)
        bag_sale.basket.set(bag_object_list)
        bag_sale_serializer = BagSaleSerializer(bag_sale)
        json.append(bag_sale_serializer.data)
    return JsonResponse(json, safe=False)


class BuySameProductsView(APIView):
    def post(self, request: Request, *args, **kwargs):
        json = _get_product(request.data, request.user)
        return json
