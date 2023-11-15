const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [n, k] = input
  .shift()
  .split(' ')
  .map((val) => +val)

const graph = Array.from(Array(n + 1), () => new Array(k + 1).fill(0))
const things = [[0, 0]]
for (let i = 0; i < n; i++) {
  things.push(
    input
      .shift()
      .split(' ')
      .map((val) => +val),
  )
}
for (let row = 1; row < n + 1; row++) {
  for (let col = 1; col < k + 1; col++) {
    w = things[row][0]
    v = things[row][1]

    if (col < w) graph[row][col] = graph[row - 1][col]
    else graph[row][col] = Math.max(graph[row - 1][col], graph[row - 1][col - w] + v)
  }
}
console.log(graph[n][k])
