from typing import Generic, TypeVar

from rest_framework import serializers

from clothing_store.serializers import FurCoatSerializer, HatSerializer, BagSerializer, GlovesSerializer
from sold_system.models import FurCoatSale, GlovesSale, HatSale, BagSale

Model = TypeVar("Model")


class GenericSerializer(serializers.ModelSerializer, Generic[Model]):
    class Meta:
        model = Model


class FurCoatSaleSerializer(GenericSerializer[FurCoatSale]):
    basket = FurCoatSerializer(many=True)

    class Meta:
        model = FurCoatSale
        fields = ('date_sell', 'basket')


class HatSaleSerializer(GenericSerializer[HatSale]):
    basket = HatSerializer(many=True)

    class Meta:
        model = HatSale
        fields = ('date_sell', 'basket')


class BagSaleSerializer(GenericSerializer[BagSale]):
    basket = BagSerializer(many=True)

    class Meta:
        model = BagSale
        fields = ('date_sell', 'basket')


class GlovesSaleSerializer(GenericSerializer[GlovesSale]):
    basket = GlovesSerializer(many=True)

    class Meta:
        model = GlovesSale
        fields = ('date_sell', 'basket')
