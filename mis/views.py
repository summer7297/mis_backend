from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

from django.http import Http404
from rest_framework.decorators import api_view


@api_view(['POST'])
def login_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        try:
            user = get_object_or_404(User, username=username)
        except Http404:
            return Response({'result': 'error', 'message': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)

        if user.password == password:
            return Response({'result': 'success', 'message': 'Valid credentials'}, status=status.HTTP_200_OK)
        else:
            return Response({'result': 'error', 'message': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
