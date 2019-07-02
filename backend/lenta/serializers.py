from rest_framework import serializers

from .models import NewsPost


class NewsPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsPost
        fields = (
                  'header',
                  'body',
                  'image',
                  'post_date',
                  )


class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsPost
        fields = (
            'header',
            'image',
            'url'
        )

