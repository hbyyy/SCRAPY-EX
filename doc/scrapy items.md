# scrapy items



### Item 만들기

**`items.py`**

```python
import scrapy


class ItArticle(scrapy.Item):
    title = scrapy.Field()
    image_url = scrapy.Field()
    contents = scrapy.Field()
```



item 클래스를 만드는 건 간단하다. 원하는 이름의 클래스를 만들고,   크롤링해 저장할 데이터 유형들을 Field 로 만들어 주면 된다.



#### item의 장점


1. 수집한 데이터를 일관성 있게 관리
2. 데이터를 Dict 형으로 관리 , 오타 방지
3. 추후 가공 및 DB 저장 용이



### Item 이용하기

- spider
- **source -> [https://itnews.com/](https://itnews.com/)  **

```python
class TestSpider(scrapy.Spider):
    name = 'test6'
    allowed_domains = ['itnews.com']
    start_urls = ['https://itnews.com/']

    def parse(self, response):
        """

        :param response:
        :return: Request
        """
        for url in response.css('section.bodee div.newsfeed').xpath(
                './div[@class="news-item"]/div[@class="hed"]//a/@href').getall():
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        """

        :param response:
        :return: Items
        """
        item = ItArticle()

        item['title'] = response.xpath('//h1[@itemprop="headline"]/text()').get()
        item['image_url'] = response.xpath('//img[@itemprop="contentUrl"]/@data-original').get()
        item['contents'] = ''.join(response.xpath('//div[@itemprop="articleBody"]/p/text()').getall()).strip()

        print(dict(item))
        yield item
```



 이용도 간단하다. 사용하고자 하는  Spider 파일에서 커스텀한 Item 클래스의 인스턴스로 생성해주면 된다.

> item class는 파이썬 기본 자료형인 Dict 와 비슷하게 동작한다. item Field에 값을 추가하는 방식도 비슷하고, dict(item) 으로 간단하게 dict 형으로 변환할 수도 있다.