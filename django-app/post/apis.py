from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
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


class PostListFindAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

    def get_queryset(self):
        search_title = self.request.query_params.get('q')
        # search_title = self.request.poster_title
        post_search = Post.objects.filter(poster_title__contains=search_title)

        return post_search

class PostLikeToggleView(APIView):
    def post(self, request, post_pk):
        post_instance = get_object_or_404(Post, pk=post_pk)
        post_like, post_like_created = post_instance.postlike_set.get_or_create(
            user=request.user
        )
        if not post_like_created:
            post_like.delete()
        return Response({'created': post_like_created})