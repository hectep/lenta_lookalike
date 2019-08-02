from datetime import datetime
import requests.api

from scrapy.http import Request
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.utils.project import get_project_settings

from ..items import NewsPostItem

LENTA_URL = get_project_settings().get('LENTA_URL')

BACKEND_LINKS_URL = get_project_settings().get('BACKEND_LINKS_URL')


def get_urls_from_database():

    resp = requests.api.get(BACKEND_LINKS_URL).json()['data']
    links = [LENTA_URL + x['url'] for x in resp]
    for link in resp:
        requests.post(
            url=f'{BACKEND_LINKS_URL}{link["pk"]}/',
            data={'is_parsed': True}
        )
    return links


class NewsPostSpider(Spider):
    """
    A spider to crawl through the links, crawled by NewsLinksSpider
    """

    name = 'NewsPost'

    def start_requests(self):
        urls = get_urls_from_database()
        for url in urls:
            yield Request(url, dont_filter=True)

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
