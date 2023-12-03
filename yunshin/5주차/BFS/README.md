# BFS (Breadth-First Search)

## 🚩 핵심 요약

- 그래프(Graph) 탐색 기법 - 그래프: 정점과 간선으로 이루어진 자료구조 - 그래프 탐색: 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한번씩 방문하는 것
<div align="center">

![그래프](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/25eab53d-eec6-4dea-a3f3-ace01453bbf9)

</div>

- 시작노드(루트 노드, Root Node) 부터 가까운 노드 순으로 방문하여 조건에 맞는 노드를 찾아낸다.
<div align="center">

![DFSvsBFS](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/5f104d23-957f-4bd9-a9dc-6230770e13e8)

</div>

- 다음으로 탐색할 노드를 queue 와 같은 자료구조에 저장해 두었다가, 현재 노드의 방문을 종료하며 저장했던 노드를 차례로 방문한다.
  - queue 는 '선입선출' 이라는 특징을 가지기 때문에 얕은 depth 의 노드부터 저장, 방문이 이뤄진다.

## 🔥 실전적용

- 주로 최단거리 문제에서 자주 사용한다.
  - 굳이 모든 노드를 방문하지 않더라도 가까운 거리의 노드부터 찾아나가기 때문에 최단거리를 구하기는 문제 유형에서는 DFS 보다 효율적이다.
- while 문과 if 문 등의 주로 사용되기 때문에 여러 분기에 대한 데이터 흐름을 제대로 이해하며 설계해야한다. (구현 연습 필요.!)

```js
const que = []
que.push(['첫 노드의 정보'])
while (que.length !== 0){
    let curNode = que.shift()
    // 탐색 종료 조건문
    if (){}
    // 현재 노드를 기준으로 탐색
   let nexNode = ['que에 저장할 노드의 정보']
   // 탐색 결과를 queue 에 저장
   que.push(nexNode)
}
```

- queue 에 저장하는 데이터 종류에 따라 효율성이 달라질 수도 있다.
