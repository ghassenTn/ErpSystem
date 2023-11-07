from django.shortcuts import render
# views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginAPI(APIView):
    def post(self, request):
        # Retrieve the entered username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authentication successful
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            # Authentication failed
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, 'index.html')
# Create your views here.
