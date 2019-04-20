from datetime import datetime

from scrapy import Spider, Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, TakeFirst, Compose
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from django.db.utils import IntegrityError
from django.conf import settings
from lenta.models import NewsLink, NewsPost


LENTA_URL = settings.LENTA_URL


def get_urls_from_database():
    urls = [LENTA_URL + url for url in NewsLink.objects.filter(
        is_parsed=False).values_list('url', flat=True) if 'news' in url]
    return urls


class NewsLinksSpider(Spider):
    """
    A spider to crawl links to the news from mainpage
    """

    name = 'News'
    start_urls = [
        LENTA_URL,
    ]

    def parse(self, response):

        items = response.css('div.span8 section.row div.span4 div.item')
        items.append(
            response.css('div.span8 section.row div.span4 div.first-item'))

        for item in items:
            a = {
                'header': item.css(
                    'a::text').extract_first(),
                'url': item.css(
                    'a::attr("href")').extract_first()
            }

            if 'news' in a['url']:
                try:
                    NewsLink.objects.get_or_create(url=a['url'])
                except IntegrityError as error:
                    print(str(error))


class NewsPostItem(Item):
    url = Field(output_processor=TakeFirst())
    db_url = Field(output_processor=TakeFirst())
    header = Field(output_processor=TakeFirst())
    body = Field(
        output_processor=Compose(Join(), lambda v: ' '.join(v.split())))
    image = Field()
    original_date = Field(output_processor=TakeFirst())
    post_date = Field(output_processor=TakeFirst())
    images = Field()
    image_urls = Field()


class NewsPostSpider(Spider):
    """
    A spider to crawl through the links, crawled by NewsLinksSpider
    """

    name = 'NewsPost'
    start_urls = get_urls_from_database()

    def parse(self, response):

        item = ItemLoader(item=NewsPostItem(), response=response)
        _url = response.url.replace(LENTA_URL, '')
        item.add_value('db_url', _url)
        item.add_value('url', _url.replace('/', '_'))
        item.add_css('header', 'h1.b-topic__title::text')
        item.add_css('body', 'div.b-text p::text')
        item.add_css('original_date', 'time.g-date::attr("datetime")')
        item.add_value('post_date', datetime.now().isoformat())
        item.add_css(
            'images',
            'div.b-topic__title-image img.g-picture::attr("src")')
        item.add_css(
            'image_urls',
            'div.b-topic__title-image img.g-picture::attr("src")')
        return item.load_item()


class NewsPostPipeline(object):

    def process_item(self, item, spider):
        item['image'] = item['images'][0]['path']
        item.pop('images')
        item.pop('image_urls')
        db_url = item.pop('db_url')
        news_post = NewsPost(**item)

        try:
            news_post.save()
            NewsLink.objects.filter(url=db_url).update(is_parsed=True)
        except IntegrityError:
            raise DropItem("Contains duplicate: %s" % item['url'][0])
        return item


class NewsImagePipeLine(ImagesPipeline):

    def process_item(self, item, spider):
        return super().process_item(item, spider)
