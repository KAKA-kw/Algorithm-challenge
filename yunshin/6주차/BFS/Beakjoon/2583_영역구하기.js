// BFS
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

for (let row = 0; row < m; row++) {
  for (let col = 0; col < n; col++) {
    if (graph[row][col] == 0) {
      graph[row][col] = 1
      let res = 0
      const que = []

      que.push([row, col])
      while (que.length) {
        const [curRow, curCol] = que.shift()
        res += 1
        for (let i = 0; i < 4; i++) {
          if (0 <= curRow + dy[i] && curRow + dy[i] < m && 0 <= curCol + dx[i] && curCol + dx[i] < n && graph[curRow + dy[i]][curCol + dx[i]] == 0) {
            graph[curRow + dy[i]][curCol + dx[i]] = 1
            que.push([curRow + dy[i], curCol + dx[i]])
          }
        }
      }
      answer.push(res)
    }
  }
}
console.log(answer.length)
console.log(answer.sort((a, b) => a - b).join(' '))
