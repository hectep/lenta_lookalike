import requests.api

from scrapy import Spider
from scrapy.utils.project import get_project_settings


LENTA_URL = get_project_settings().get('LENTA_URL')

BACKEND_LINKS_URL = get_project_settings().get('BACKEND_LINKS_URL')


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
            link = {
                'header': item.css(
                    'a::text').extract_first(),
                'url': item.css(
                    'a::attr("href")').extract_first()
            }

            requests.api.post(BACKEND_LINKS_URL, data={'url': link['url']})
