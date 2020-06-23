# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SiteRankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    site_name = scrapy.Field()
    daily_time_site = scrapy.Field()
    daily_page_view = scrapy.Field()

    ## 파이프라인 통과했는지 알기 위한 필드
    is_pass = scrapy.Field()
