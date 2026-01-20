from django.db.models import ProtectedError
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from inventory_app import models
from inventory_app import serializers


@api_view(['GET', 'POST'])
def items_list(request):
    if request.method == 'GET':
        items = models.Item.objects.all()
        serializer = serializers.ItemSerializer(instance=items, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = serializers.ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def item(request, pk: int):
    inventory_item = get_object_or_404(models.Item, id=pk)

    if request.method == 'GET':
        serializer = serializers.ItemSerializer(instance=inventory_item)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.ItemSerializer(instance=inventory_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inventory_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerializer(instance=categories, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category(request, pk: int):
    inventory_category = get_object_or_404(models.Category, id=pk)

    if request.method == 'GET':
        serializer = serializers.CategorySerializer(instance=inventory_category)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.CategorySerializer(instance=inventory_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        try:
            inventory_category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
