const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const graph = input.map((row) => row.split(' ').map((col) => +col))

const problems = []
for (let row = 0; row < 9; row++) {
  for (let col = 0; col < 9; col++) {
    if (!graph[row][col]) problems.push([row, col])
  }
}
function check(row, col, n) {
  for (let i = 0; i < 9; i++) {
    if (graph[row][i] == n) return false
  }
  for (let i = 0; i < 9; i++) {
    if (graph[i][col] == n) return false
  }

  const startRow = Math.floor(row / 3) * 3
  const startCol = Math.floor(col / 3) * 3

  for (let i = startRow; i < startRow + 3; i++) {
    for (let j = startCol; j < startCol + 3; j++) {
      if (graph[i][j] == n) return false
    }
  }
  return true
}
const backTracking = (depth) => {
  if (depth === problems.length) {
    console.log(graph.map((col) => col.join(' ')).join('\n'))
    process.exit(0)
  }
  const [row, col] = problems[depth]
  for (let val = 1; val <= 9; val++) {
    if (check(row, col, val)) {
      graph[row][col] = val
      backTracking(depth + 1)
      graph[row][col] = 0
    }
  }
}
backTracking(0)
