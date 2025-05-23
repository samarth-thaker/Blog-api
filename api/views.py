from django.shortcuts import render
from rest_framework import viewsets
from .models import Articles
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all().order_by('-published_date')
    serializer_class = ArticleSerializer

