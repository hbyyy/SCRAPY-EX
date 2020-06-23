## 한 요소에 class가 여러개일 때 선택하기

예시

```
<div class="class1 class2">1</div>
```



### css 이용

- xpath보다 간편하다.

```
div.class1.class2
```



### xpath 이용

- css보다 번거롭고 복잡하다.
- 크롤링시 클래스가 여러개 붙어있는 요소를 크롤링 해야하면 css로 선택하는게 좋을 것 같다.

```
//div[contains(@class, 'class1') and contains(@class, 'class2')]

//div[starts-with(@class, "class1")]

```

???

div[@class="class1 class2"] 그냥 이렇게 해도 되는 것 같다.



## selector 헷갈리는 요소

### 자식 선택 vs 자손 선택

- css와 xpath 동시에 사용하다 보니 헷갈린다..

| css   | xpath | 의미                        |
| ----- | ----- | --------------------------- |
| A   B | A//B  | A의 **자손** 요소 중 B 선택 |
| A > B | A/B   | A의 **자식** 요소 중 B 선택 |

