# -*- coding: utf-8 -*-
import scrapy

from ..items import SiteRankItem


class TestSpider(scrapy.Spider):
    name = 'test10'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['https://alexa.com/topsites/']

    def parse(self, response):
        for contents in response.css('div.listings div.site-listing'):
            item = SiteRankItem()
            item['rank'] = contents.xpath('./div[1]/text()').get()
            item['site_name'] = contents.css('div.td.DescriptionCell').xpath('./p/a/text()').get()
            item['daily_time_site'] = contents.xpath('./div[3]/p/text()').get()
            item['daily_page_view'] = contents.xpath('./div[4]/p/text()').get()

            yield item
