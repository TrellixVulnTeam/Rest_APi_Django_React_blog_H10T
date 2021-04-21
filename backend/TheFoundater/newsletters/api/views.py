from rest_framework import viewsets
from .serializers import News_serializers
from ..models import Newsletter


class NewsView(viewsets.ModelViewSet):
    serializer_class = News_serializers
    queryset = Newsletter.objects.all()
