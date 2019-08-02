from scrapy import Item, Field
from scrapy.loader.processors import Join, TakeFirst, Compose


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
