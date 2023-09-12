# BFS (Breadth-First Search, 너비 우선 탐색)

<p align="center"><img src="https://velog.velcdn.com/images%2Fsukong%2Fpost%2F103fbeed-3f70-4074-9a7d-76915a7764f2%2FBFS.png" width="60%" /></p>

BFS는 깊이가 가장 얕은 노드부터 모두 탐색한 뒤 깊이가 깊은 노드를 탐색하는 방법이다. 즉, 그림에서 깊이가 1인 노드1과 노드2를 먼저 탐색한 뒤, 깊이가 1인 노드를 모두 탐색하였으므로 깊이가 2인 노드인 노드3, 노드4, 노드5, 노드6을 탐색하는 순서이다.

## BFS의 특징

- 두 노드 사이의 최단 경로를 탐색할 때 활용하기 좋은 방식이다. 멀리 떨어진 노드는 나중에 탐색하기 때문이다.
- 큐를 활용할 때 탐색할 노드의 순서를 저장하고 큐에 저장된 순서대로 탐색한다. 선입선출의 방식을 활용하기 때문에 큐를 활용한다.

## BFS 구현 알고리즘

1. 루트노드에서 시작한다.
2. 루트노드와 인접하고 방문된 적 없고, 큐에 저장되지 않은 노드를 큐에 넣는다.
3. 큐에 dequeue하여 가장 먼저 큐에 저장한 노드를 방문한다.

<img src="https://gmlwjd9405.github.io/images/algorithm-dfs-vs-bfs/bfs-example.png">

## BFS 구현

#### 1. 시작 노드인 0을 큐에 삽입하고 방문 처리한다.

<img src="https://chamdom.blog/static/0ee9abfcfba8e99b76d8f222ad8f87ee/e85cb/bfs-step1.png">

#### 2. 큐에서 0을 꺼내고 방문하지 않은 인접 노드 1, 2, 4를 큐에 삽입하고 모두 방문 처리한다.

<img src="https://chamdom.blog/static/da8f99057f742f67d42c2af2c0a85e05/e85cb/bfs-step2.png">

#### 3. 큐에서 1을 꺼내고 방문하지 않은 인접 노드 5를 큐에 삽입하고 방문 처리한다.

<img src="https://chamdom.blog/static/12147d6c14248ebe0ffcdf62b3c102e0/e85cb/bfs-step3.png">

#### 4. 큐에서 2를 꺼내고 방문하지 않은 인접 노드가 없으므로 무시한다.

<img src="https://chamdom.blog/static/a541f031a08b382304005f28ca23d9d7/e85cb/bfs-step4.png">

#### 5. 큐에서 4를 꺼내고 방문하지 않은 인접 노드 3을 큐에 삽입하고 방문 처리한다.

<img src="https://chamdom.blog/static/eb3be361ceb153868759efd4c53f8bc2/e85cb/bfs-step5.png">

#### 6. 남아 있는 노드에 방문하지 않은 인접 노드가 없다. 따라서 모든 노드를 큐에서 차례대로 꺼낸다.

<img src="https://chamdom.blog/static/bdc0d31b1239c4ea1a76866375e16498/e85cb/bfs-step6.png">

결과적으로 그래프의 탐색 순서는 다음과 같다.

0 → 1 → 2 → 4 → 5 → 3

## JavaScript로 구현하는 BFS

```js
function BFS(graph, start, visited) {
  const queue = new Queue()
  queue.push(start)
  visited[start] = true

  while (queue.size()) {
    const v = queue.popleft()
    console.log(v)

    for (const node of graph[v]) {
      if (!visited[node]) {
        queue.push(node)
        visited[node] = true
      }
    }
  }
}

const graph = [[1, 2, 4], [0, 5], [0, 5], [4], [0, 3], [1, 2]]
const visited = Array(6).fill(false)
BFS(graph, 0, visited)
// 0 1 2 4 5 3
```
