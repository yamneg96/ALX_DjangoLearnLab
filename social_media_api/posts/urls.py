# posts/urls.py (add feed)
from django.urls import path, include
from .views import FeedView, PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename="post")
router.register(r'comments', CommentViewSet, basename="comment")

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
]
