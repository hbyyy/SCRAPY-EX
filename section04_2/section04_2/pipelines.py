from scrapy.exceptions import DropItem


class TestSpiderPipeline:
    # spider 시작시 1번 실행됨
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Started')

    def process_item(self, item, spider):
        if int(item.get('rank')) < 41:
            item['is_pass'] = True
            return item
        else:
            raise DropItem(f'Dropped Item. Because This site rank is {item.get("rank")}')

    def close_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Closed')
