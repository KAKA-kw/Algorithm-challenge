// BFS
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [n, m] = input
  .shift()
  .split(' ')
  .map((i) => +i)
const graph = []
graph.push(new Array(m + 1).fill(0))
for (let att = 0; att < n; att++) {
  const row = input
    .shift()
    .split('')
    .map((i) => +i)
  row.unshift(0)
  graph.push(row)
}

const dyDx = [
  [0, 1],
  [0, -1],
  [-1, 0],
  [1, 0],
]
const que = []
que.push([1, 1])
while (que.length) {
  const [cy, cx] = que.shift()
  for (const [dy, dx] of dyDx) {
    if (0 <= cy + dy && cy + dy <= n && 0 <= cx + dx && cx + dx <= m && graph[cy + dy][cx + dx] === 1) {
      graph[cy + dy][cx + dx] = graph[cy][cx] + 1
      que.push([cy + dy, cx + dx])
    }
  }
}

console.log(graph[n][m])
