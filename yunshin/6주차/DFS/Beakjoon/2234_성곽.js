// DFS
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [m, n] = input
  .shift()
  .split(' ')
  .map((i) => +i)
const dxDy = [
  [-1, 0],
  [0, -1],
  [1, 0],
  [0, 1],
]
const 소인수분해 = (num) => {
  const res = new Array(4).fill(0)
  for (let i = 0; i < 4; i++) {
    res[i] = !(num % 2)
    num = Math.floor(num / 2)
  }
  return res
}
const graph = []
while (input.length) {
  const row = input
    .shift()
    .split(' ')
    .map((i) => +i)
  graph.push(row)
}
const visited = new Array(n).fill().map(() => new Array(m).fill(0))

const DFS = (cy, cx, val, id) => {
  let res = 1
  const 분해결과 = 소인수분해(val)
  for (let i = 0; i < 4; i++) {
    if (분해결과[i]) {
      const [dx, dy] = dxDy[i]
      if (0 <= cy + dy && cy + dy < n && 0 <= cx + dx && cx + dx < m && visited[cy + dy][cx + dx] == 0) {
        visited[cy + dy][cx + dx] = id
        res += DFS(cy + dy, cx + dx, graph[cy + dy][cx + dx], id)
      }
    }
  }
  return res
}

const roomSizes = {}
let id = 1
for (let row = 0; row < n; row++) {
  for (let col = 0; col < m; col++) {
    if (visited[row][col] == 0) {
      visited[row][col] = id
      roomSizes[id] = DFS(row, col, graph[row][col], id)
      id++
    }
  }
}

// 합쳐서 최대
let previous = 1
let maxSizeAfterAdd = -1
//가로
for (let row = 0; row < n; row++) {
  previous = visited[row][0]
  for (let col = 0; col < m; col++) {
    if (previous != visited[row][col]) {
      maxSizeAfterAdd = Math.max(roomSizes[visited[row][col]] + roomSizes[previous], maxSizeAfterAdd)
      previous = visited[row][col]
    }
  }
}
//세로
for (let col = 0; col < m; col++) {
  previous = visited[0][col]
  for (let row = 0; row < n; row++) {
    if (previous != visited[row][col]) {
      maxSizeAfterAdd = Math.max(roomSizes[visited[row][col]] + roomSizes[previous], maxSizeAfterAdd)
      previous = visited[row][col]
    }
  }
}
console.log(Object.keys(roomSizes).length)
console.log(Math.max(...Object.values(roomSizes)))
console.log(maxSizeAfterAdd)
