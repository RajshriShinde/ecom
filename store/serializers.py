from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'description', 'created_at', 'updated_at']


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['id', 'title', 'created_at', 'updated_at', 'available_for_sale', 'price']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'product', 'source', 'alt_text', 'uploaded_at']


class CollectionSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Collection
        fields = ['id', 'products', 'title', 'published', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'parent']


class ProductCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCollection
        fields = ['id', 'product', 'collection']
