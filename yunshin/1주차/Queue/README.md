# 큐(Queue)

## 핵심 요약

- 선입선출 (FIFO)

<div align="center">

![큐](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/34d14efa-0cbd-440f-9ddd-8e013bba76b0)

</div>

## 실전적용 (Python 기준)

- list 보다 deque(double-ended queue, 양방향에서 추가/삭제 가능) 으로 구현하는 것이 훨씬 경제적!!
  - 이유는 list 로 구현하고 맨 앞으로 요소를 `pop(0)` (삭제) / `insert(0)` (추가) 할 경우, 모든 원소들의 인덱스를 수정해주는 작업이 필요하다.
    - _시간복잡도 => O(n)_
  - deque 는 (Doubly Linked List)양방향 연결리스트로 구현되어 있어, 원소의 추가/삭제 외에 부수적인 작업을 최소화할 수 있다.
    - _시간복잡도 => O(1)_
