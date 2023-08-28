# 해쉬테이블(HashTable)

## 핵심 요약

- Key-Value 구조를 가지는 자료구조
- Data 를 삽입하거나 읽는 것이 굉장히 빠르다. => O(1)
- Value 는 데이터 타입에 따라 중복이 가능할 수도 있지만, Key 간에는 절대 중복이 있어서는 안된다.

<div align="center">

![해쉬테이블](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/00d6fc91-ab54-4c6d-a617-01315f555c61)

</div>

## 실전적용 (Python 기준)

- key 와 value 의 선정하는 것에 고민 필요..
- value 의 타입이 list 일 경우, 정렬 알고리즘을 도입하는 문제가 많다.
- 파이썬에서 dictionary 라고 부르는데, 저장되는 데이터 타입의 제약이 없다.
- value 값의 타입을 일치시키기 위해, collections.defaultdict 라이브러리를 자주 이용한다.
