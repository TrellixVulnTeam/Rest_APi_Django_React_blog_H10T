from rest_framework import viewsets
from .serializers import Post_serializers
from ..models import Post


class PostView(viewsets.ModelViewSet):
    serializer_class = Post_serializers
    queryset = Post.objects.all()
