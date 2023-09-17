# DFS (Depth-First Search)

## 🚩 핵심 요약

- 그래프(Graph) 탐색 기법
  - 그래프: 정점과 간선으로 이루어진 자료구조
  - 그래프 탐색: 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한번씩 방문하는 것

<div align="center">

![그래프](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/25eab53d-eec6-4dea-a3f3-ace01453bbf9)

</div>

- 시작노드(루트 노드, Root Node) 부터 가까운 노드 순으로 방문하여 조건에 맞는 노드를 찾아낸다.

<div align="center">

![DFSvsBFS](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/5f104d23-957f-4bd9-a9dc-6230770e13e8)

</div>

- 현재 방문한 노드의 자식을 우선적으로 탐색, 방문한다.
- 스택 또는 재귀함수로 구현

## 🔥 실전적용

- 현재 값을 기준으로 계속 연산을 해야하는 경우, 재귀호출을 이용하여, 해결할 수 있다.
- 리프노드(자식이 더이상 없는 노드) 에 대한 분기처리를 확실히 해주어야., 무한 호출이 발생하지 않는다.

```js
// dfs 기본골격

function dfs(부모노드까지의_결과) {
  if (리프노드_라면) {
    return
  } // 리프노드에 대한 분기 처리
  if (타겟노드_라면) {
  } // 조건에 맞는 노드를 찾았을 때의 분기처리
  const 현재노드까지의_결과 = 부모노드가지의_결과 + 현재노드에서의_어떤_값
  dfs(현재노드까지의_결과) // 자식노드로 현재까지의 연산결과를 넘긴다.
}
```
