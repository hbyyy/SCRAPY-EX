# Scrapy Shell

## Scrapy Shell 이란?

- Shell에서 스크리패 코드를 테스트 해 볼 수 있는 환경이다





## 시작하기

**`scrapy shell`**





## Shell 에서 쓸 수 있는 커맨드

### fetch(url)

- 해당 url 의 소스를 가져온다

- 크롤링 코드를 테스트하기 위한 첫번째 과정



#### response

- fetch로 가져온 응답이 저장된다.
- response.body, response.status, response.headers 등의 정보를 사용 가능

**`dir(response)`**

```python
['_DEFAULT_ENCODING', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_auto_detect_fun', '_body', '_body_declared_encoding', '_body_inferred_encoding', '_cached_benc', '_cached_selector', '_cached_ubody', '_declared_encoding', '_encoding', '_get_body', '_get_url', '_headers_encoding', '_set_body', '_set_url', '_url', 'body', 'body_as_unicode', 'cb_kwargs', 'certificate', 'copy', 'css', 'encoding', 'flags', 'follow', 'follow_all', 'headers', 'ip_address', 'meta', 'replace', 'request', 'selector', 'status', 'text', 'url', 'urljoin', 'xpath']
```





### view(response)

- response의 내용을 브라우저로 열어줌





###  robots.txt

Scrapy는 해당 사이트의 robots.txt를 읽어서 크롤링한 대상들을 정한다.

만약 사이트에 robots.txt 가 없거나, 루트 단위에서 막혀있다면 크롤링을 제대로 하지 않을 것이다.

사이트의 robots.txt 를 무시하는 커맨드도 존재한다.

**`scrapt <명령어> --set="ROBOTSTXT_OBEY=False"`**

> scrapy project의 settings.py에서 ROBOTSTXT_OBEY 값을 False로 지정해 주어도 똑같다.



