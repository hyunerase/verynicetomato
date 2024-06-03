from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class BlogList(ListCreateAPIView): #커스텀할게 많을 때에는 APIView로 하는게 좋다
    queryset = Blog.objects.all() #G
    serializer_class = BlogSerializer #C,R
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer): #실질적 save
        user = self.request.user
        serializer.save(user=user)

class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]