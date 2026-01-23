from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users_app.models import CustomUser
from users_app.serializers import UserRegisterSerializer, LoginSerializer, UserUpdateSerializer
from rest_framework.authtoken.models import Token


#user registration view
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, create = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    user_instance = get_object_or_404(CustomUser, id=pk)
    serializer = UserUpdateSerializer(instance=user_instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
