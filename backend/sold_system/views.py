import uuid
from typing import List, Tuple

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.request import Request
from django.db.models import Model

from authentication.models import User
from backend.settings import Products
from clothing_store.models import FurCoat, Gloves, Bag, Hat, Size
from sold_system.models import FurCoatSale, HatSale, BagSale, GlovesSale
from sold_system.serializers import FurCoatSaleSerializer, HatSaleSerializer, BagSaleSerializer, GlovesSaleSerializer
import enum


class FurCoatSaleViewSet(viewsets.ModelViewSet):
    queryset = FurCoatSale.objects.all()
    serializer_class = FurCoatSaleSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(seller=request.user)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class HatSaleViewSet(viewsets.ModelViewSet):
    queryset = HatSale.objects.all()
    serializer_class = HatSaleSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(seller=request.user)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class BagSaleViewSet(viewsets.ModelViewSet):
    queryset = BagSale.objects.all()
    serializer_class = BagSaleSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(seller=request.user)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class GlovesSaleViewSet(viewsets.ModelViewSet):
    queryset = GlovesSale.objects.all()
    serializer_class = GlovesSaleSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(seller=request.user)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


def _get_model_object(product: dict, product_model: Model) -> Model:
    product_id = product.get("product_id")
    product_object = get_object_or_404(product_model, pk=product_id)
    return product_object


def _get_product(products: List[dict], user: User) -> JsonResponse:
    fur_coats_object_list = list()
    hat_object_list = list()
    gloves_object_list = list()
    bag_object_list = list()
    json = []
    for product in products:
        match product.get("type"):
            case Products.fur_coat.value:
                fur_coat = _get_model_object(product, FurCoat)
                size = Size.objects.get(
                    pk=fur_coat.product.sizesproduct_set.get(size_id=product.get("size_id")).size_id)
                if size.count < 0:
                    return JsonResponse(
                        {"error": "Товара такого размера нет в наличии"})
                if product.get("count") > size.count:
                    return JsonResponse(
                        {"error": "Отстутствует такое количество товаров"})
                size.count -= product.get("count")
                size.save()
                fur_coats_object_list.append({"furcoat": fur_coat, "count": product.get("count")})
            case Products.gloves.value:
                gloves = _get_model_object(product, Gloves)
                size = Size.objects.get(
                    pk=gloves.product.sizesproduct_set.get(size_id=product.get("size_id")).size_id)
                if size.count < 0:
                    return JsonResponse(
                        {"error": "Товара такого размера нет в наличии"})
                if product.get("count") > size.count:
                    return JsonResponse(
                        {"error": "Отстутствует такое количество товаров"})
                size.count -= product.get("count")
                size.save()
                gloves_object_list.append({"gloves": gloves, "count": product.get("count")})
            case Products.bag.value:
                bag = _get_model_object(product, Bag)
                bag.count -= product.get("count")
                bag.save()
                bag_object_list.append({"bag": bag, "count": product.get("count")})
            case Products.hat.value:
                hat = _get_model_object(product, Hat)
                size = Size.objects.get(
                    pk=hat.product.sizesproduct_set.get(size_id=product.get("size_id")).size_id)
                if size.count < 0:
                    return JsonResponse(
                        {"error": "Товара такого размера нет в наличии"})
                if product.get("count") > size.count:
                    return JsonResponse(
                        {"error": "Отстутствует такое количество товаров"})
                size.count -= product.get("count")
                size.save()
                hat_object_list.append({"hat": hat, "count": product.get("count")})
    if fur_coats_object_list:
        total_furcoat_count = sum([i.get("count") for i in fur_coats_object_list])
        fur_coat_sale = FurCoatSale.objects.create(seller=user, count=total_furcoat_count)
        fur_coat_sale.basket.set([i.get("furcoat") for i in fur_coats_object_list])
        fur_coat_serializer = FurCoatSaleSerializer(fur_coat_sale)
        json.append(fur_coat_serializer.data)
    if hat_object_list:
        total_hat_count = sum([i.get("count") for i in hat_object_list])
        hat_sale = HatSale.objects.create(seller=user, count=total_hat_count)
        hat_sale.basket.set([i.get("hat") for i in hat_object_list])
        hat_sale_serializer = HatSaleSerializer(hat_sale)
        json.append(hat_sale_serializer.data)
    if gloves_object_list:
        total_gloves_count = sum([i.get("count") for i in gloves_object_list])
        gloves_sale = GlovesSale.objects.create(seller=user, count=total_gloves_count)
        gloves_sale.basket.set([i.get("gloves") for i in gloves_object_list])
        gloves_sale_serializer = GlovesSaleSerializer(gloves_sale)
        json.append(gloves_sale_serializer.data)
    if bag_object_list:
        total_bag_count = sum([i.get("count") for i in bag_object_list])
        bag_sale = BagSale.objects.create(seller=user, count=total_bag_count)
        bag_sale.basket.set([i.get("bag") for i in bag_object_list])
        bag_sale_serializer = BagSaleSerializer(bag_sale)
        json.append(bag_sale_serializer.data)
    return JsonResponse(json, safe=False)


class BuySameProductsView(APIView):
    def post(self, request: Request, *args, **kwargs):
        json = _get_product(request.data, request.user)
        return json
