from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from post.serializers import PostSerializer, PostCreateSerializer
from utilt.permissions import ObjectIsRequestUser
from .models import Post


class PostListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        ObjectIsRequestUser,
    )
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer


class PostUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
