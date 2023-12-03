# Map

순차적으로 메모리에 데이터를 저장하는 배열과는 달리 `Key`와 `Value`로 구성되어 있는 개념의 자료구조

<p align="center"><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ft7Q78%2FbtriSLD4MK1%2FHC4rv3LgSoEbDq4xYUbuz1%2Fimg.png" width="50%"/></p>

## Map 특징

```
1️⃣ Key(키)와 Value(값)이 쌍으로 이루어져 있다.
```

```
2️⃣ Key의 중복을 허용하지 않는다.
```

```
3️⃣ 탐색이 빠르다.

    Map은 해시 테이블 등의 자료 구조를 사용하여 데이터를 관리
    → 특정 키에 대한 값에 직접 접근 가능
    → 요소를 찾아내는 탐색 작업에서는 일반적으로 Map이 배열보다 더 빠른 성능
```

## Map은 왜 사용하는가?

```
⭐️ 순서보다는 정의된 이름(Key)과 상응하는 데이터들을 묶기 위해 효과적!
```

## JavaScript에서 Map 사용하기

### Map 객체 생성

```js
const myMap = new Map()
```

### key, value를 set 하기

```js
myMap.set('A', 'valueA')
```

### key로 value get하기

```js
myMap.get('A')
```

### key와 value delete하기

```js
myMap.delete('A')
```

### 해당 키가 Map에 존재하는지 확인하기

```js
myMap.has('A') // boolean
```

### 모든 원소 제거하기

```js
myMap.clear()
```

### [키, 값] 형태의 중첩 배열 → Map으로

```js
const array = [
  ['A', 'valueA'],
  ['B', 'valueB'],
  ['C', 'valueC'],
]

const myMap = new Map(array)
```

# 참고

- [자료구조 - Map(맵)](https://blog-of-gon.tistory.com/187)
- [JavaScript Map 데이터 구조 사용법 한 번에 정리하기: 생성, set, get, has, delete, clear](https://kotlinworld.com/414)
