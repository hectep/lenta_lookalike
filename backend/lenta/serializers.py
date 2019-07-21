from rest_framework.serializers import ModelSerializer

from .models import NewsPost, NewsLink


class NewsPostSerializer(ModelSerializer):

    class Meta:
        model = NewsPost
        fields = (
                  'header',
                  'body',
                  'image',
                  'post_date',
                  )


class NewsListSerializer(ModelSerializer):

    class Meta:
        model = NewsPost
        fields = (
            'header',
            'image',
            'url'
        )


class CreateNewsSerializer(ModelSerializer):

    class Meta:
        model = NewsPost
        fields = (
            'header',
            'image',
            'url',
            'post_date',
            'original_date',
            'body'
        )


class NewsLinkSerializer(ModelSerializer):

    class Meta:
        model = NewsLink
        fields = (
            'url',
            'is_parsed',
            'pk'
        )