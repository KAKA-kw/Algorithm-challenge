# 스택(Stack)

## 핵심 요약

- 후입선출 (LIFO)

<div align="center">

![스택](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/4b1ce7fc-8920-4307-8ee5-1841f9e69bfc)

</div>

## 실전적용 (Python 기준)

- list 로 구현해도 좋다.
  - 구조가 단순
  - 탐색이 빠르다.!
  - 맨 뒤로 요소를 추가/삭제 하는 것은 앞선 요소에 영향 x
- 단, underflow, overflow 와 같은 구조 크기 관련 문제에 집중해야한다.
  - 입/출력 시, 각 상황에 대한 분기점을 우선 구현하는 것이 안전.!
