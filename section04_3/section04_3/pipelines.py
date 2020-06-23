import csv

import xlsxwriter
from scrapy.exceptions import DropItem


class TestSpiderPipeline:

    def __init__(self):
        # 엑셀 처리 선언
        self.workbook = xlsxwriter.Workbook('result_excel.xlsx')
        # csv 처리 선언(a, w 옵션 변경)
        self.file_opener = open('result_csv.csv', 'w')
        self.csv_writer = csv.DictWriter(self.file_opener,
                                         fieldnames=['rank', 'site_name', 'daily_time_site', 'daily_page_view',
                                                     'is_pass'])
        # worksheet
        self.worksheet = self.workbook.add_worksheet()
        # 삽입 수 카운트
        self.rowcount = 1

    # spider 시작시 1번 실행됨
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Started')

    def process_item(self, item, spider):
        if int(item.get('rank')) < 41:
            item['is_pass'] = True

            # 엑셀 저장
            self.worksheet.write('A%s' % self.rowcount, item.get('rank'))
            self.worksheet.write('B%s' % self.rowcount, item.get('site_name'))
            self.worksheet.write('C%s' % self.rowcount, item.get('daily_time_site'))
            self.worksheet.write('D%s' % self.rowcount, item.get('daily_page_view'))
            self.worksheet.write('E%s' % self.rowcount, item.get('is_pass'))
            self.rowcount += 1

            # csv 저장
            self.csv_writer.writerow(item)
            return item
        else:
            raise DropItem(f'Dropped Item. Because This site rank is {item.get("rank")}')

    def close_spider(self, spider):
        # 엑셀 파일 닫기
        self.workbook.close()
        self.file_opener.close()

        spider.logger.info('TestSpider Pipeline Closed')
