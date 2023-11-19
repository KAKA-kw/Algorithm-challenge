# 덱(Deque)

```
⭐️ Double Ended Queue
   양쪽 끝에서 삽입과 삭제가 전부 가능한 자료구조

   → 데이터를 양방향으로 다루어야 하는 상황에서 유용
```

<p align="center"><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F22370A4558CFD0FA17" width="40%"/></p>

# 덱의 성질

```
1. 추가/삭제 : O(1)
2. 맨 앞/뒤 조회 : O(1)
```

# 덱 구현

```js
const deque = []

// 맨 앞 삽입
deque.unshift(data)

// 맨 뒤 삽입
deque.push(data)

// 맨 앞 삭제
deque.shift()

// 맨 뒤 삭제
deque.pop()
```
