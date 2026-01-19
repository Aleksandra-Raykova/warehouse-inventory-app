from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users_app.serializers import UserSerializer


#user registration view
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create user logout
#login
#edit
#delete
