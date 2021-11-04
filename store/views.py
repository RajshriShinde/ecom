from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import *
from django.db.models.functions import Concat
from django.db.models import Value as V, F
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .serializers import (ProductSerializer, VariantSerializer, ImageSerializer, CollectionSerializer,
                          CategorySerializer, UserSerializer)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_list(request):

    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif User.is_staff:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_detail(request, pk):
    print(request.method)
    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.user.is_staff:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ProductSerializer(product, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            product.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def variant_list(request):

    if request.method == 'GET':
        variant = Variant.objects.all()
        serializer = VariantSerializer(variant, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.user.is_staff:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = VariantSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def variant_detail(request, pk):
    try:
        variant = Variant.objects.get(pk=pk)

    except Variant.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VariantSerializer(variant)
        return JsonResponse(serializer.data)

    elif request.user.is_staff:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = VariantSerializer(variant, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            variant.delete()
            return Response(status=204)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def image_list(request):

    if request.method == 'GET':
        image = Image.objects.all()
        serializer = ImageSerializer(image, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.user.is_staff:
        if request.method == 'POST':
            serializer = ImageSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def image_detail(request, pk):
    try:
        image = Image.objects.get(pk=pk)

    except Image.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ImageSerializer(image)
        return JsonResponse(serializer.data)

    elif request.user.is_staff:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ImageSerializer(image, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            image.delete()
            return HttpResponse(status=204)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def collection_list(request):
    if request.method == 'GET':
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.user.is_staff:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = CollectionSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def collection_detail(request, pk):
    try:
        collection = Collection.objects.get(pk=pk)

    except Collection.DoNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return JsonResponse(serializer.data)

    elif request.user.is_staff:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = CollectionSerializer(collection, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            collection.delete()
            return HttpResponse(status=204)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CollectionSerializer(category, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.user.is_staff:
        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = CategorySerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)

    except Category.DoNotExist:
        HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CollectionSerializer(category)
        return JsonResponse(serializer.data)

    elif request.user.is_staff:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = CategorySerializer(category, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            category.delete()
            return HttpResponse(status=204)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_of_product_of_collections(request, pk):
    if request.method == 'GET':
        list_of_products = list(Product.objects.values('title', 'description', 'created_at', 'updated_at')
                                                               .filter(collections=pk).annotate(_images=F('images')))
        serializer = ProductSerializer(list_of_products, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_of_variants_of_collection(request, pk):
    if request.method == 'GET':
        list_of_variants = Variant.objects.annotate(_title=Concat('product__title',
                                                        V(" "), 'title')).filter(product__collections=pk)

        serializer = VariantSerializer(list_of_variants, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_of_variants_of_category(request, pk):
    category = Category.objects.get(id=pk)
    variants = category.all_variants.annotate(_title=Concat('product__title', V(" "), 'title'))
    serializer = VariantSerializer(variants, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_email(request, pk):
    try:
        user = User.objects.get(pk=pk)

    except User.DoNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.user.is_staff:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = UserSerializer(user, data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

