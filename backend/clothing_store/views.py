from rest_framework import viewsets
from clothing_store.models import FurCoat, Hat, Bag, Gloves
from clothing_store.serializers import FurCoatSerializer, GlovesSerializer, HatSerializer, BagSerializer


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
