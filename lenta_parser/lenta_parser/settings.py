import os

BOT_NAME = 'lenta_parser'

SPIDER_MODULES = ['lenta_parser.spiders']

NEWSPIDER_MODULE = 'lenta_parser.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'lenta_parser.pipelines.NewsPostPipeline': 300,
   'lenta_parser.pipelines.NewsImagePipeLine': 200,
}

IMAGES_STORE = '/home/nester/work/portfolio/first/lenta_lookalike/lenta_parser/media'

LENTA_URL = os.environ['LENTA_URL']

BACKEND_LINKS_URL = os.environ['BACKEND_LINKS_URL']

BACKEND_CREATE_NEWS_URL = os.environ['BACKEND_CREATE_NEWS_URL']
