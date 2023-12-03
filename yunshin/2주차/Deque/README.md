# 덱(Deque)

## 핵심 요약

- 양방향으로 데이터의 삽입, 제거가 가능한 자료구조
- 배열 / 연결리스트로 구현 가능

  - 이중연결리스트(DoublyLinked List): 각 노드가 서로 연결되어 있어, 단일연결리스트보다 탐색이 유리하고 노드의 추가/삭제가 배열보다는 단순할 수 있다.

  - 단, 노드 저장에 필요한 메모리가 다른 구조보다 크고, 구현이 복잡하다는 단점이 있다. 그럼에도 장점이 크기 때문에 현실에서 사용하는 연결리스트는 대부분 이중연결 리스트이다.

<div align="center">

![덱](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/35998894-5442-4cb9-ac40-67d3cbf54c74)
![이중연결리스트](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/6080fc60-22c4-4bb8-8c1e-e01f27b6ee84)

</div>

## 실전적용 (Python 기준)

- queue , stack 관련 문제에 적용하여 문제를 해결할 수 시간 복잡도 상에서 얻을 수 있다. (queue 관련 문제는 필수다.! 안쓰면 시간초과 뜨기도..)

  - queue 관련 문제(백준-요세푸스 문제)를 list로 구현하여 풀었을 때,
    <img width="1136" alt="스크린샷 2023-08-28 오후 9 32 25" src="https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/aaa21b1a-4813-41db-991c-73f3affc6f97">

  - 위와 같은 문제를 deque 라이브러리를 임포트하여 풀었을 때,
    <img width="1139" alt="스크린샷 2023-08-28 오후 9 32 31" src="https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/4f7c11cc-2c72-49d1-964a-50e3e73a60bf">
