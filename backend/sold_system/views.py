from rest_framework import viewsets

from sold_system.models import FurCoatSale, HatSale, BagSale, GlovesSale
from sold_system.serializers import FurCoatSaleSerializer, HatSaleSerializer, BagSaleSerializer, GlovesSaleSerializer


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
