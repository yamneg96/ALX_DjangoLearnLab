from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

class FeedView(APIView):
    def get(self, request):
        # posts by users I follow
        following_ids = request.user.following.values_list("id", flat=True)
        qs = Post.objects.filter(author_id__in=following_ids).order_by("-created_at")
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(qs, request)
        serializer = PostSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


# Custom permission: only owners can edit/delete their own posts/comments
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS → allow for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise → only the owner can modify
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
