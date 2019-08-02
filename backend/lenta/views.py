from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import CursorPagination
from rest_framework.parsers import MultiPartParser
from .models import NewsPost, NewsLink
from .serializers import (NewsPostSerializer, NewsListSerializer,
                          CreateNewsSerializer, NewsLinkSerializer)
from .renderers import NewsPostJSONRenderer


class NewsListPagination(CursorPagination):
    """
    A pagination used in NewsViewSet
    """
    page_size = 4
    ordering = '-post_date'


class NewsViewSet(ModelViewSet):
    """
    ViewSet to work with actual news
    """

    pagination_class = NewsListPagination
    serializer_class = NewsPostSerializer
    renderer_classes = (NewsPostJSONRenderer,)
    parser_classes = (MultiPartParser, )
    queryset = NewsPost.objects.all()
    paginate_by_param = 'page_size'

    serializers = {
        'default': NewsListSerializer,
        'create': CreateNewsSerializer,
        'list': NewsListSerializer,
        'retrieve': NewsPostSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])


class NewsLinkViewSet(ModelViewSet):
    """
    ViewSet for NewsLink model,
    used to monitor, which news were already parsed
    """
    serializer_class = NewsLinkSerializer
    renderer_classes = (NewsPostJSONRenderer,)

    def get_queryset(self):
        """
        we need only unparsed links which belong to news (not articles etc.)
        """
        return NewsLink.objects.filter(
            is_parsed=False, url__istartswith='/news')
