# 큐(Queue)

```
⭐️ 큐는 선입선출(First In First Out, FIFO)이다!
```

## 🤔 큐의 작동원리

```
⭐️ 선입선출!
   → 가장 먼저 들어온 데이터가 가장 먼저 빠져나가야 하는 구조
```

## 🤔 큐의 시간복잡도

```
⭐️ 삽입/삭제 → O(1)
   탐색 → O(n)
```

### 그런데, 자바스크립트에서는요

```
⭐️ 자바스크립트에서 객체는 key-value의 구조로 사용할 수 있다!
   → key값을 통해 O(1) 시간으로 접근이 가능
```

## 🤔 자바스크립트에서 Queue 구현

알고리즘 문제에서 알맞게 사용하기 위해 메소드의 구현체를 살펴보았습니다.

```js
export default class Queue {
  constructor() {
    // item들을 받을 배열 생성
    this.items = []
  }

  enqueue(item) {
    this.items.push(item)
  }

  dequeue() {
    return this.items.shift()
  }

  peek() {
    return this.items[0]
  }

  getSize() {
    return this.items.length
  }

  isEmpty() {
    return this.getSize() === 0
  }
}
```
