from scrapy.pipelines.images import ImagesPipeline
from requests.api import post
from scrapy.utils.project import get_project_settings

BACKEND_CREATE_NEWS_URL = get_project_settings().get('BACKEND_CREATE_NEWS_URL')

BACKEND_LINKS_URL = get_project_settings().get('BACKEND_LINKS_URL')

STORE_PATH = get_project_settings().get('IMAGES_STORE')


class NewsPostPipeline(object):

    def process_item(self, item, spider):
        img = item['images'][0]['path']
        item.pop('images')
        item.pop('image_urls')
        with open(f'{STORE_PATH}/{img}', 'rb') as file:
            post(
                url=BACKEND_CREATE_NEWS_URL,
                data=dict(item),
                files={'image': file}
            )

        return item


class NewsImagePipeLine(ImagesPipeline):

    def process_item(self, item, spider):
        return super().process_item(item, spider)
