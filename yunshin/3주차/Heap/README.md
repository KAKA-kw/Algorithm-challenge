# Heap

## 핵심 요약

- 완전 이진 트리의 일종
  - 완전 이진 트리란, 가장 아래에 있는 depth 를 제외하고 모든 depth 의 노드가 자식노드를 두개씩 가지고 있는 트리
  - 가장 깊은 depth 에서도 왼쪽에 있는 노드부터 값이 채워져 있어야 한다.

<div align="center">

![완전이진트리](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/c888e662-28cf-4131-8f8d-ebbd3aa3d792)

</div>

- 최댓값, 최솟값을 찾거나 정렬 목적으로 사용한다.

  - 힙 구조를 거친 데이터들은 우선순위에 따라 하나씩 값을 출력할 수 있기 때문이다.
  - 최댓값, 최솟값을 찾을 때 순차탐색으로는 **O(n)** 이나 힙을 이용하면, **O(n)** 으로 단축할 수 있다.
  - 힙 정렬(heap sort) 는 가장 많이 사용되는 쿽 정렬(quick sort) 보다 아주 약간 느리지만, 입력과 동시에 정렬을 하는 경우 등 상황에 따라 고려 가능한 옵션이다.

  <div align="center">

![정렬법_간_시간복잡도](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/de44f507-0a6f-4cc5-8b4e-560c52f85cec)

  </div>

## 실전적용 (Python 기준)

- 주로 heapq 라이브러리를 import 하여 사용한다.
- 이 경우, Max_Heap 이 지원되지 않는다.
  - (-1) 을 곱하면 Min_Heap 으로 최댓값을 찾을 수 있다.
- Heap의 크기를 무한정 키우는 것은 공간,시간 효율성을 떨어뜨린다.
  - 크기를 일정하게 제한할 수 있는 방법을 고려하는 것이 좋다.
  - ex) 백준\_2075 문제 참고
- 최솟값(혹은 최댓값) 을 확인만 하려는 목적으로, 값을 꺼내는 것은 좋지 못하다.
  - heap 구조에서 최솟값(혹은 최댓값) 은 가장 상위 노드에 있으므로 리스트의 첫번째 원소를 확인하면 된다.

<br/>

_Heap 의 값을 꺼내서 비교하고 다시 push 한 경우_

<div align="center">

  <img width="593" alt="스크린샷 2023-09-03 오후 8 11 20" src="https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/19cd0815-a4a4-4f76-b11f-0c937e58b3ae">

  <img width="684" alt="스크린샷 2023-09-03 오후 8 14 38" src="https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/e64ba45c-cbd1-4bbe-a7e9-d16619df6f5f">
  
</div>

<br/>

_최상단의 값을 확인하고, 필요한 경우에만 pop & push_

<div align="center">

  <img width="571" alt="스크린샷 2023-09-03 오후 8 13 40" src="https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/e41a8d1c-6c80-4b1e-b356-db06e3b2864f">

  <img width="703" alt="스크린샷 2023-09-03 오후 8 14 33" src="https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/98870427-9842-4bbf-aa76-2f449b4359a4">  
  
</div>
