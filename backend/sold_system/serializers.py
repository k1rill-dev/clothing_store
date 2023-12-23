from typing import Generic, TypeVar

from rest_framework import serializers

from authentication.serializers import UserSerializer
from clothing_store.serializers import FurCoatSerializer, HatSerializer, BagSerializer, GlovesSerializer
from sold_system.models import FurCoatSale, GlovesSale, HatSale, BagSale

Model = TypeVar("Model")


class GenericSerializer(serializers.ModelSerializer, Generic[Model]):
    class Meta:
        model = Model


class FurCoatSaleSerializer(GenericSerializer[FurCoatSale]):
    basket = FurCoatSerializer(many=True)
    seller = UserSerializer()

    class Meta:
        model = FurCoatSale
        fields = ('id', 'date_sell', 'basket', 'seller')


class HatSaleSerializer(GenericSerializer[HatSale]):
    basket = HatSerializer(many=True)
    seller = UserSerializer()

    class Meta:
        model = HatSale
        fields = ('id', 'date_sell', 'basket', 'seller')


class BagSaleSerializer(GenericSerializer[BagSale]):
    basket = BagSerializer(many=True)
    seller = UserSerializer()

    class Meta:
        model = BagSale
        fields = ('id', 'date_sell', 'basket', 'seller')


class GlovesSaleSerializer(GenericSerializer[GlovesSale]):
    basket = GlovesSerializer(many=True)
    seller = UserSerializer()

    class Meta:
        model = GlovesSale
        fields = ('id', 'date_sell', 'basket', 'seller')
