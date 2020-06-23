# Scrapy Export

여태까지 파일을 저장할 때는

**`scrapy crawl test4 -o result.jl -t jsonlines`**

이런 식으로 커맨드를 사용해 결과를 저장했다.



이번 챕터에서는 export 기능을 이용해 파일을 자동으로 저장해 볼 것이다.





### Feed Exports

- [Scrapy 문서 Feed exports](https://docs.scrapy.org/en/latest/topics/feed-exports.html)




#### 출력 형식
   1. JSON, JSON Lines
   2. CSV
   3. XML, Pickle, Marshal



#### 저장 위치
   1. Local File System (My PC)
   2. FTP - (Server)
   3. S3 - (AWS)
   4. 기본 콘솔



#### 방법
   1. 커맨드 이용
       - ((--output, -o) , (--output-format, -t)) 
       - 옵션 설정 예 -> --set=FEED_EXPORT_INDENT = 2
       
   2. settings.py 에 설정
       - 자동으로 저장 (파일명, 형식, 위치)



**`settings.py`**

```python
...
# Export setting

# 파일이름 및 경로
FEED_URI = 'result.json'

# 파일 형식
FEED_FORMAT = 'json'

# 출력 인코딩
FEED_EXPORT_ENCODING = 'utf-8'

# 기본 들여쓰기
# json 이나 xml 형식일 때만 적용된다
FEED_EXPORT_INDENT = 2
```

