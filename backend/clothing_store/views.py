from uuid import UUID

from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from django.db.models import Model
from rest_framework.request import Request

from clothing_store.models import FurCoat, Hat, Bag, Gloves, AbstractProduct, PhotoFurCoat, PhotoGloves, PhotoHat, \
    PhotoBag
from clothing_store.serializers import FurCoatSerializer, GlovesSerializer, HatSerializer, BagSerializer, \
    PhotoFurCoatSerializer, PhotoGlovesSerializer, PhotoHatSerializer, PhotoBagSerializer


class FurCoatViewSet(viewsets.ModelViewSet):
    queryset = FurCoat.objects.all()
    serializer_class = FurCoatSerializer


class HatViewSet(viewsets.ModelViewSet):
    queryset = Hat.objects.all()
    serializer_class = HatSerializer


class BagViewSet(viewsets.ModelViewSet):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


class GlovesViewSet(viewsets.ModelViewSet):
    queryset = Gloves.objects.all()
    serializer_class = GlovesSerializer


class PhotoFurCoatView(APIView):
    def get(self, request: Request, *args, **kwargs):
        data = request.data
        fur_coat = get_object_or_404(FurCoat, pk=data.get('id'))
        photos = PhotoFurCoat.objects.filter(fur_coat=fur_coat)
        photos_serializer = PhotoFurCoatSerializer(photos, many=True)
        return JsonResponse(photos_serializer.data, safe=False)


class PhotoGlovesView(APIView):
    def get(self, request: Request, *args, **kwargs):
        data = request.data
        gloves = get_object_or_404(Gloves, pk=data.get('id'))
        photos = PhotoGloves.objects.filter(gloves=gloves)
        photos_serializer = PhotoGlovesSerializer(photos, many=True)
        return JsonResponse(photos_serializer.data, safe=False)


class PhotoHatView(APIView):
    def get(self, request: Request, *args, **kwargs):
        data = request.data
        hat = get_object_or_404(Hat, pk=data.get('id'))
        photos = PhotoHat.objects.filter(hat=hat)
        photos_serializer = PhotoHatSerializer(photos, many=True)
        return JsonResponse(photos_serializer.data, safe=False)


class PhotoBagView(APIView):
    def get(self, request: Request, *args, **kwargs):
        data = request.data
        bag = get_object_or_404(Bag, pk=data.get('id'))
        photos = PhotoBag.objects.filter(bag=bag)
        photos_serializer = PhotoBagSerializer(photos, many=True)
        return JsonResponse(photos_serializer.data, safe=False)
