from django.shortcuts import render
from apiusers.serializers import AdminSerializer, UserSerializer
from desafio.permissions import IsAdmin, IsAdminOrReadOnly
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.


class APICreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class APICreateAdmin(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated,IsAdmin]