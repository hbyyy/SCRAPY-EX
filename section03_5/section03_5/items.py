
"""
item 을 사용할 때 장점
    1. 수집한 데이터를 일관성 있게 관리
    2. 데이터를 Dict 형으로 관리 , 오타 방지
    3. 추후 가공 및 DB 저장 용이
"""
import scrapy


class ItArticle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    contents = scrapy.Field()
