from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lenta_lookalike.settings')
app = Celery('test')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
scrapy_settings = get_project_settings()


@app.task()
def parse_news_list():
    """
    Task parses links to the news and stores them in db to parse later
    """

    from lenta.parsers.lenta_parser import NewsLinksSpider

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    })

    process.crawl(NewsLinksSpider)
    process.start()


@app.task()
def parse_news_post():
    """
    Task parses news using the links of unparsed news stored in db
    """

    from lenta.parsers.lenta_parser import NewsPostSpider

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'ITEM_PIPELINES': '{'
                          '"lenta.parsers.lenta_parser.NewsImagePipeLine": 1,'
                          '"lenta.parsers.lenta_parser.NewsPostPipeline": 2}',
        'IMAGES_STORE': settings.MEDIA_ROOT,
    })

    process.crawl(NewsPostSpider)
    process.start()


app.conf.beat_schedule = {
    "parse links periodic task": {
        "task": "lenta.celery.parse_news_list",
        "schedule": 30.0
    },
    "parse post periodic task": {
        "task": "lenta.celery.parse_news_post",
        "schedule": 30.0
    },
}

