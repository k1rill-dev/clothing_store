import inspect
import pprint
import sys
from uuid import UUID

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from django.db.models import Model
from rest_framework.request import Request

from backend.settings import Products
from clothing_store import models, serializers
from clothing_store.models import FurCoat, Hat, Bag, Gloves, AbstractProduct, PhotoFurCoat, PhotoGloves, PhotoHat, \
    PhotoBag, Product
from clothing_store.serializers import FurCoatSerializer, GlovesSerializer, HatSerializer, BagSerializer, \
    PhotoFurCoatSerializer, PhotoGlovesSerializer, PhotoHatSerializer, PhotoBagSerializer


class FurCoatViewSet(viewsets.ModelViewSet):
    queryset = FurCoat.objects.all()
    serializer_class = FurCoatSerializer

    def list(self, request, *args, **kwargs):
        fur_coats = FurCoat.objects.all()
        data = []
        for fur_coat in fur_coats:
            photos = list()
            photos_object = PhotoFurCoat.objects.filter(fur_coat=fur_coat)
            photos.append(PhotoFurCoatSerializer(photos_object, many=True).data)
            data.append({
                **FurCoatSerializer(fur_coat).data,
                "photos": photos
            })
        return JsonResponse(data, safe=False)


class HatViewSet(viewsets.ModelViewSet):
    queryset = Hat.objects.all()
    serializer_class = HatSerializer

    def list(self, request, *args, **kwargs):
        hats = Hat.objects.all()
        data = []
        for hat in hats:
            photos = list()
            photos_object = PhotoHat.objects.filter(hat=hat)
            photos.append(PhotoHatSerializer(photos_object, many=True).data)
            data.append({
                **HatSerializer(hat).data,
                "photos": photos
            })
        return JsonResponse(data, safe=False)


class BagViewSet(viewsets.ModelViewSet):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer

    def list(self, request, *args, **kwargs):
        bags = Bag.objects.all()
        data = []
        for bag in bags:
            photos = list()
            photos_object = PhotoBag.objects.filter(bag=bag)
            photos.append(PhotoBagSerializer(photos_object, many=True).data)
            data.append({
                **BagSerializer(bag).data,
                "photos": photos
            })
        return JsonResponse(data, safe=False)


class GlovesViewSet(viewsets.ModelViewSet):
    queryset = Gloves.objects.all()
    serializer_class = GlovesSerializer

    def list(self, request, *args, **kwargs):
        gloves = Gloves.objects.all()
        data = []
        for glove in gloves:
            photos = list()
            photos_object = PhotoGloves.objects.filter(gloves=glove)
            photos.append(PhotoGlovesSerializer(photos_object, many=True).data)
            data.append({
                **GlovesSerializer(glove).data,
                "photos": photos
            })
        return JsonResponse(data, safe=False)
