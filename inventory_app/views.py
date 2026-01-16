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
