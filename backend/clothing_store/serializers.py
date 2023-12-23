from rest_framework import serializers

from .models import FurCoat, Hat, Bag, Gloves, Product, Material, ManufacturerCountry, Brand, Season, Size, \
    PhotoFurCoat, PhotoGloves, PhotoHat, PhotoBag, SizesProduct


class PhotoFurCoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoFurCoat
        exclude = ("fur_coat",)


class PhotoGlovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGloves
        exclude = ("gloves",)


class PhotoHatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoHat
        exclude = ("hat",)


class PhotoBagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoBag
        exclude = ("bag",)


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ("size", "count", "id")


class ProductSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)

    class Meta:
        model = Product
        fields = ("title", "color", "description", "sizes", "date_of_receipt")


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        exclude = ("id",)


class ManufacturerCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturerCountry
        exclude = ("id",)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        exclude = ("id",)


class FurCoatSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    manufacturer = serializers.CharField(source='manufacturer.manufacturer')
    season = serializers.CharField(source='season.season')
    brand = serializers.CharField(source='brand.brand')
    material = serializers.CharField(source='material.title')

    class Meta:
        model = FurCoat
        fields = (
            'id', "price", "product", 'manufacturer', 'season', 'brand', 'material', 'removable_part', 'hood', 'clasp',
            'length', 'shadow', 'collar_style')


class HatSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    manufacturer = serializers.CharField(source='manufacturer.manufacturer')
    season = serializers.CharField(source='season.season')
    brand = serializers.CharField(source='brand.brand')
    material = serializers.CharField(source='material.title')

    class Meta:
        model = Hat
        fields = (
            'id', "price", "product", 'manufacturer', 'season', 'brand', 'material')


class BagSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    manufacturer = serializers.CharField(source='manufacturer.manufacturer')
    season = serializers.CharField(source='season.season')
    brand = serializers.CharField(source='brand.brand')
    material = serializers.CharField(source='material.title')

    class Meta:
        model = Bag
        fields = (
            'id', "price", "product", 'manufacturer', 'season', 'brand', 'material', 'clasp', 'width',
            'width_of_bottom',
            'height', 'belt', 'equipment', 'legs', 'inside_pockets_count',
        )


class GlovesSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    manufacturer = serializers.CharField(source='manufacturer.manufacturer')
    season = serializers.CharField(source='season.season')
    brand = serializers.CharField(source='brand.brand')
    material = serializers.CharField(source='material.title')

    class Meta:
        model = Gloves
        fields = (
            'id', "price", "product", 'manufacturer', 'season', 'brand', 'material')
