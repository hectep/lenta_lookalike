from django.db import models


class NewsPost(models.Model):
    """
    A model to store news.
    """

    url = models.CharField('URL', primary_key=True, max_length=100, unique=True)
    header = models.CharField('Header', max_length=200)
    body = models.CharField('Body', max_length=4000)
    image = models.ImageField('Image', default='default/default_news_image.jpg')
    original_date = models.DateTimeField('Date posted on lenta.ru')
    post_date = models.DateTimeField('Date posted on this site')

    def __unicode__(self):
        return self.header

    def __str__(self):
        return self.header

    class Meta:

        verbose_name_plural = verbose_name = 'News'


class NewsLink(models.Model):
    """
    A stub model for parsing news from lenta
    """

    url = models.CharField('URL', max_length=100, unique=True)
    is_parsed = models.BooleanField(default=False)

