# Scrapy Pipeline

[ Scrapy Pipeline 문서](https://docs.scrapy.org/en/latest/topics/item-pipeline.html)



##  pipeline의 일반적인 용도

- cleansing HTML data
- validating scraped data (checking that the items contain certain fields)
- checking for duplicates (and dropping them)
- storing the scraped item in a database

또 SMS 전송, SNS 전송, 메일 발송 등을 하고 싶을 때 pipeline에 정의해 주면 된다.



 크롤링한 데이터를 item에 넣어 pipeline에 보내고, pipeline에서 이 데이터들을 **정제** 해서 저장한다.



## 구현 방법

`project/project/pipelines.py`에 정의해주면 된다.



### 메소드

- pipeline에는 정의할 수 있는 4가지 메소드가 있다.
  
  1. process_item**(** *self* **,** *item* **,** *spider* **)**
  
  2. open_spider**(** *self* **,** *spider***)**
  3. close_spider(self, spider)
  4. from_crawler(cls, crawler)



#### open_spider(self, spider)

- 최초에 1회 실행된다



#### close_spider(self, spider)

- 마지막에 1회 실행된다.





#### process_item(self, item, spider) -> 가장 중요

- spider가 크롤링해 넘겨준 item을 처리하는 코드를 작성한다!

##### DropItem

- exeption
- 버릴 데이터가 오면, 이 exeption을 일으켜 준다.
- log에 dropitem이라고 표시된다!





### settings.py 설정

 구현한 pipeline을 적용하려면, settings.py 에서 관련 설정을 추가해 줘야 한다.

- **`settings.py`**

```python
ITEM_PIPELINES = {
   'section04_2.pipelines.TestSpiderPipeline': 300,
    ....
}
```

- key:value 형식으로 설정해 준다
  - value는 **우선순위** 숫자이다. **값이 낮을수록** 먼저 실행된다!!.



### code

```python
from scrapy.exceptions import DropItem


class TestSpiderPipeline:
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

```

