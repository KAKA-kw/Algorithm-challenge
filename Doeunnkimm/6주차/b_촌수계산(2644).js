const input = require('fs').readFileSync('./input/b_2644.txt').toString().trim().split('\n')

const n = +input[0] // 전체 사람 수
const [p, q] = input[1].split(' ').map(Number) // p, q 두 사람의 번호
const m = +input[2] // 관계의 개수
const arr = input.slice(3).map((v) => v.split(' ').map(Number)) // 부모-자식 관계 배열

let visited = Array(n + 1).fill(false)
let graph = [...Array(n + 1)].map(() => [])

arr.map(([from, to]) => {
  graph[from].push(to)
  graph[to].push(from)
})

// DFS
const dfs = (start, target) => {
  const queue = [[start, 0]]
  visited[start] = true

  while (queue.length) {
    const [curNum, depth] = queue.shift()
    if (curNum === target) return depth

    for (const node of graph[curNum]) {
      if (!visited[node]) {
        visited[node] = true
        queue.push([node, depth + 1])
      }
    }
  }
  return -1
}

console.log(dfs(p, q))
