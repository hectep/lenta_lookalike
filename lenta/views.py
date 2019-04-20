from rest_framework import generics
from rest_framework.pagination import CursorPagination

from .models import NewsPost
from .serializers import NewsPostSerializer, NewsListSerializer
from .renderers import NewsPostJSONRenderer


class NewsListPagination(CursorPagination):
    """
    A pagination used in NewsList view
    """
    page_size = 3
    ordering = '-post_date'


class NewsList(generics.ListAPIView):

    queryset = NewsPost.objects.all()
    serializer_class = NewsListSerializer
    renderer_classes = (NewsPostJSONRenderer,)
    paginate_by = 2
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    pagination_class = NewsListPagination


class NewsPostDetail(generics.RetrieveAPIView):

    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    renderer_classes = (NewsPostJSONRenderer, )
