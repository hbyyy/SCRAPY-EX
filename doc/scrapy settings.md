# Scrapy settings



- settings.py 에는 주석 처리되어 있는 많은 코드들이 있다.
- 이 세팅 코드들을 설정하면 더 효율적으로 크롤링을 할 수 있다.



## scrapy 환경설정

### 실행 방법

1. 커맨드 라인 실행
   - `scrapy crawl <spider name> -s (--set) NAME=VALUE`



2. Spider 실행 시 직접 지정

   - `*spider.py`

     - ```python
       class TestSpuder(scrapy.Spider):
       	....
       	
       	custom settings = {
       		'NAME1': VALUE1,
       		'NAME2': VALUE2,
       		...
       	}
       ```



3. **settings.py 에 지정** -> 추천 방법
4. 서브 명령어
5. 글로벌 설정
   - scrapy.settings.default_settings을 불러와 설정한다.







## settings.py 살펴보기



### settings.py의 KEYWORD

많은 키워드들이 있다. 기본적으로 주석처리 되어 있는 키워드들 말고도 여러 키워드가 있으니 공식문서를 확인하자

[Scrapy 공식문서 settings](https://docs.scrapy.org/en/latest/topics/settings.html#)



다음은 자주 사용되는 키워드들이다.



#### CONCURRENT_REQUESTS

- 병렬 처리하는 request의 수를 정해준다
- default 는 16개



#### DOWNLOAD_DELAY

- 소스 다운로드 딜레이 시긴을 정할 수 있다.
  - 너무 적은 시간에 너무 많은 양의 요청을 보낸다면, 크롤링할 사이트에서 block을 먹을 수 있으므로 적당히 조정하자!
- 2 나 1로 많이 둔다.



#### CONCURRENT_REQUESTS_PER_DOMAIN

- 웹 사이트 도메인 동시 병렬 처리 개수
- default = 16



#### CONCURRENT_REQUESTS_PER_IP

- 특정 웹 사이트 ip 주소 병렬 처리 개수
- default = 16



#### COOKIES_ENABLED

- 쿠기 활성화 여부를 설정한다
- 만약 403 이 뜬다면 True로 설정해 보자



#### DEFAULT_REQUEST_HEADERS

- 기본 request 헤더값을 설정할 수 있다.

- 기본값

  - ```python
    DEFAULT_REQUEST_HEADERS = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'en',
    }
    ```



#### SPIDER_MIDDLEWARES

- 커스텀 middleware를 사용하려면 설정해 주어야 한다.



#### ITEM_PIPELINES

- 파이프라인 설정



### cache 사용여부 설정 -> 중요

```python
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
```



 캐시를 사용하면 동일하게 여러번 요청하는 작업 시 서버 부하를 절감할 수 있다.



#### HTTPCACHE_ENABLED

- 캐시 사용여부 설정 (True, False)



#### HTTPCACHE_EXPIRATION_SECS

- 캐시 초기화 시간을 설정 
- 초 단위로 설정 가능



#### HTTPCACHE_DIR

- 캐시 저장 경로를 설정한다.



#### HTTPCACHE_IGNORE_HTTP_CODES

- 응답 거부 캐시



#### HTTPCACHE_STORAGE





### 캐시 설정 on 시

- 크롤링을 수행하면, settings.py에 설정한 경로에 캐시를 만든다.

```
scrapyEx
	|- section04_1 
		|- .scrapy
			|- httpcache	-> settings.py에서 정해 준 이름
				|- 			-> 캐시가 생긴다!
					....
		|- section04_1
        |- spider
        	|- __init__.py
        	|- class04_1.py
        |- __init__.py
        |- items.py
        |- middlewares.py
        |- pipelines.py
        |- settins.py
	|- scrapy.cfg
```



캐시가 만들어지면, 똑같은 크롤링 코드를 돌렸을 때 크롤링한 코드에 변경사항이 없다면 빠르게 작업이 끝나게 된다!



### 오류 처리, 자동 재시도 설정

#### RETRY_ENABLED

- 오류나 에러시 다시 시도할 수 있도록 설정한다
- True, False

#### RETRY_TIMES

- 재시도 횟수를 설정할수 있다
- `RETRY_TIMES = <number>`

#### RETRY_HTTP_CODES 

- 재시도할 오류 status code를 정해줄 수 있다
- list 형식으로 설정
  - ex : `RETRY_HTTP_CODES = [404, 500, 502, 503, ...]`

#### HTTPERROR_ALLOWED_CODES

- 무시할 오류를 정해줄 수 있다
- 여기 설정한 오류 코드를 만나도 크롤링을 계속 진행한다
  - ex: `HTTPERROR_ALLOWED_CODES=[404, ....]`

#### HTTPERROR_ALLOWED_ALL (사용하지 않는 걸 추천)

- 모든 에러를 무시한다
- True, False