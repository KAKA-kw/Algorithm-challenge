// DFS
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [m, n, k] = input
  .shift()
  .split(' ')
  .map((x) => +x)

const graph = Array.from(Array(m), () => new Array(n).fill(0))

for (let i = 0; i < k; i++) {
  const [x1, y1, x2, y2] = input
    .shift()
    .split(' ')
    .map((x) => +x)
  for (let row = y1; row < y2; row++) {
    for (let col = x1; col < x2; col++) {
      graph[row][col] = 1
    }
  }
}

const dy = [0, 0, -1, 1]
const dx = [1, -1, 0, 0]
let answer = []

const DFS = (row, col) => {
  let subRes = 1
  for (let i = 0; i < 4; i++) {
    if (0 <= row + dy[i] && row + dy[i] < m && 0 <= col + dx[i] && col + dx[i] < n && graph[row + dy[i]][col + dx[i]] == 0) {
      graph[row + dy[i]][col + dx[i]] = 1
      subRes += DFS(row + dy[i], col + dx[i])
    }
  }
  return subRes
}
for (let row = 0; row < m; row++) {
  for (let col = 0; col < n; col++) {
    if (graph[row][col] == 0) {
      graph[row][col] = 1
      let res = DFS(row, col)
      answer.push(res)
    }
  }
}

console.log(answer.length)
console.log(answer.sort((a, b) => a - b).join(' '))
