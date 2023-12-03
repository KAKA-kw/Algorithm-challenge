# DFS (Depth-First Search, 깊이 우선 탐색)

```
📌 깊은 부분을 우선적으로 탐색하는 알고리즘

   한 노드를 시작으로 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색

   트리를 탐색할 때 시작 노드에서 한 방향으로 계속 탐색하다가 더 이상 갈 수 없을 때
   다시 가장 가까운 노드로 되돌아와 다시 탐색을 진행하는 방법
```

## DFS 동작 과정

1. 탐색 시작 노드 정보를 스택에 삽입하고 방문 처리한다.
2. 스택 내 최상단 노드에 방문하지 않은 노드가 있다면 그 인접 노드 정보를 스택에 삽입하고 방문 처리한다.
   만일 방문하지 않은 인접 노드가 없다면 스택 내 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

현재 처리 중인 노드를 파란색🔵으로 방문 처리한 노드를 회색⚪️으로 하여 DFS를 이해해보자.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Flq08u%2FbtqZpVT6mNm%2Fmp2CoBzL8ORUkkHThUR9D0%2Fimg.png">

#### 1. 시작 노드인 노드 1을 스택에 삽입하고 방문 처리한다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FzthIP%2FbtqZqou3pPx%2FN2gv0WbKhYwhAifcrVaC6k%2Fimg.png">

#### 2. 스택 내 최상단 노드인 노드 1에 인접한 노드는 2, 3이 있다. 번호가 낮은 노드 2를 스택에 삽입하고 방문 처리한다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdS7i3q%2FbtqZpfFkQMI%2F13Ek9ajk4xzn8XkC9q1iUK%2Fimg.png">

#### 3. 스택 내 최상단 노드인 노드 6에 인접하며 방문하지 않은 노드 7을 스택에 삽입하고 방문 처리한다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fd4KCbA%2FbtqZBdMvuQa%2FlSPMtmkgmYzSsL0PtpzEy0%2Fimg.png">

#### 4. 스택 내 최상단 노드인 노드 8에 인접한 노드는 6과 7이 있으며, 번호가 낮은 노드 6을 스택에 삽입하고 방문 처리한다

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FKvrhs%2FbtqZtzpYpvU%2FnrZ0QS6q3iWkEVniQOh6bK%2Fimg.png">

#### 5. 스택 내 최상단 노드인 노드 6에 인접하며 방문하지 않은 노드 7을 스택에 삽입하고 방문 처리한다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbpwr9d%2FbtqZDOM8RF3%2FfqoeWSuxbybeYfhx8pQH40%2Fimg.png">

#### 6. 최상단 노드인 노드 7에 인접하며 방문하지 않은 노드가 없으므로 스택에서 노드 7을 꺼낸다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbFumSH%2FbtqZyvtO0PQ%2FV0KWWX6xqAOriFbIkz6Rp0%2Fimg.png">

#### 7. 최상단 노드인 노드 6에 인접하며 방문하지 않은 노드가 없으므로 스택에서 노드 6을 꺼낸다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FEwkBc%2FbtqZty5MaTb%2F1hpcd2eOGpOqovABpdaSC0%2Fimg.png">

#### 8. 최상단 노드인 노드 8에도 인접하며 방문하지 않은 노드가 없으므로 스택에서 노드 8을 꺼낸다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FDrTdw%2FbtqZBcU6CSz%2FUWVPSMc1jnmLQSTofFzJu0%2Fimg.png">

#### 9. 최상단 노드인 노드 2에 인접하며 방문하지 않은 노드가 없으므로 스택에서 노드 2를 꺼낸다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQiTDP%2FbtqZBc8Bj87%2FtMYqXILhlXm2ogP99mpBCK%2Fimg.png">

#### 10. 노드 1에 인접하면서 방문 이력이 없는 노드 3을 스택에 삽입하고 방문 처리한다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbtxx4I%2Fbtq2yvxvKa6%2FYzk09LUb9UKRg2QR2sN8m1%2Fimg.png">

#### 11. 노드 3에 인접하면서 방문하지 않은 노드는 노드 4와 5가 있지만, 번호가 낮은 노드 4를 스택에 삽입하고 방문 처리한다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcJDoiA%2Fbtq2ynfij5W%2FpLUkeYZUawcXIwZvv5Zk10%2Fimg.png">

#### 12. 노드 4에 인접한 노드 5를 스택에 넣고 방문 처리한다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb2ahMy%2Fbtq2u3aLcSQ%2FaW6oY5IDJfVkjKD7zJXdkK%2Fimg.png">

#### 13. 이제 방문하지 않은 노드가 없기 때문에 스택에서 모든 노드를 차례대로 꺼낸다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb3PfNx%2FbtqZrfSQKi9%2FuwypNp6Ih3PKV7iIxXEaLK%2Fimg.png">

## JavaScript로 구현하는 DFS

### 재귀를 이용한 DFS

1. 방문 여부를 기록하기 위해 배열 visited를 사용하며, 배열 visited의 값을 false로 초기화한다.
2. 노드를 방문할 때마다 해당 노드의 visited 배열 값을 true로 변경한다.
3. 해당 노드(v)와 연결된 노드 중에 방문하지 않은 노드(node)이 있다면 방문하지 않은 노드(node)를 시작점으로 하여 DFS를 다시 시작한다.

<p align="center"><img src="https://chamdom.blog/static/5c91cb22edabbf0a610064ca9c6bdbc1/13ae7/dfs_bfs.png" width="60%"/></p>

```js
function dfs(graph, v, visited) {
  // 현재 노드를 방문 처리
  visited[v] = true
  console.log(v)

  // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for (let node of graph[v]) {
    if (!visited[node]) {
      dfs(graph, node, visited)
    }
  }
}

const graph = [[1, 2, 4], [0, 5], [0, 5], [4], [0, 3], [1, 2]]
const visited = Array(7).fill(false)

dfs(graph, 0, visited)
// 0 1 5 2 4 3
```

### 스택을 이용한 DFS

1. 스택에 시작 노드를 push 한다.
2. 스택에서 노드를 pop하고 해당 노드(v)가 방문하지 않은 노드라면 방문처리 한다.
3. 노드(v)와 연결된 노드 중에서 방문하지 않은 노드(node)이 있다면 stack에 push 한다.
4. 스택의 길이가 0이 될 때까지 2, 3번 과정을 반복한다.

```js
function dfs(graph, start, visited) {
  const stack = []
  stack.push(start)

  while (stack.length) {
    let v = stack.pop()
    if (!visited[v]) {
      console.log(v)
      visited[v] = true

      for (let node of graph[v]) {
        if (!visited[node]) {
          stack.push(node)
        }
      }
    }
  }
}
const graph = [[1, 2, 4], [0, 5], [0, 5], [4], [0, 3], [1, 2]]
const visited = Array(7).fill(false)

dfs(graph, 0, visited)
// 0 4 3 2 5 1
```

## BF와 DFS의 차이점

```
BF: 모든 가능성을 검사한다.
DFS: 특정 경로를 깊게 추적한다.
```

## 🤔 어떤 상황에서 BF와 DFS를 구분해서 사용해야 할까?

- 문제가 그래프나 트리 형태의 데이터 구조에서 발생하며, 해결책이 특정 경로에 존재할 가능성이 크다면 DFS를 사용한다.
- 문제가 모든 가능한 조합을 고려해야 하는 경우나 최적화 문제 등에 대해서는 BF 방법론이 적용될 수 있다.
