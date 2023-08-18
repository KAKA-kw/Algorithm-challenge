# 스택(Stack)

```
⭐️ 스택은 후입선출(Last-In-Fist-Out, LIFO)이다!
```

## 🤔 스택의 작동원리

```
⭐️ 후입선출!
   먼저 들어갈수록 나중에 나올 수 있는 구조로 이루어져 있다.
```

<p align="center"><img src="https://blog.kakaocdn.net/dn/SupXO/btrBxbxj1Uo/yxmSlpUTKqxY5fbAUwzJRK/img.jpg" width="60%"/></p>

## 🤔 스택의 시간복잡도

```
⭐️ 조회 → O(n)
   삽입/삭제 → O(1)
```

스택의 삽입이나 삭제는 맨 위의 데이터를 바로 조작하기 때문에 시간복잡도는 늘 `O(1)`이다. 하지만 특정 데이터를 찾을 때까지 순차적으로 수행해야 하므로 `O(n)`의 시간 복잡도를 갖는다.

### 🙌 그런데 JavaScript에서는요

```
⭐️ 자바스크립트는 배열이 동적 배열로 구현
   → 인덱스로 바로 접근하는 경우, 조회 시에도 시간복잡도가 O(1)
```

## 🤔 스택의 사용 사례 (후입선출)

- 웹 브라우저 방문기록(뒤로가기)
- 실행 취소(undo)(되돌리기)
- 역순 문자열 만들기

## 🤔 스택을 언제 활용하면 좋을까?

```
1. 기저 조건에 도달한 후 결과를 차례대로 반환해 나갈 때
2. 순차적으로 바로 이전 조건을 확인하며 나아갈 때
3. 순차적으로 반대로 접근해야 할 때

등등
```

## 🤔 JavaScript에서 스택을 활용해보자

```js
const stack = []

// 데이터 삽입
stack.push(1)
stack.push(2)
stack.push(3)

// 최상단 데이터 확인 (삭제하지 않음)
const top = stack.at(-1)
console.log(top) // 3

// 데이터 삭제
const poppedValue = stack.pop()
console.log(poppedValue) // 3

// Stack이 비어 있는지 확인
const isEmpty = stack.length === 0
console.log(isEmpty) // false

// Stack 크기 확인
const size = stack.length
console.log(size) // 2
```
