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
        return Response(serializer.data)


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
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        inventory_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
