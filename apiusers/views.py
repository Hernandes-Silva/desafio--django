from django.shortcuts import render
from rest_framework.response import Response
from apiusers.serializers import AdminSerializer, UserSerializer
from desafio.permissions import IsAdmin, IsAdminOrReadOnly
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
# Create your views here.
class APICreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class APICreateAdmin(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = User.objects.all()
    serializer_class = AdminSerializer

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)