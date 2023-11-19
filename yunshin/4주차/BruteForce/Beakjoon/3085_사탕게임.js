const input = require('fs').readFileSync('yunshin/4주차/BruteForce/Beakjoon/input/b_3085.txt').toString().trim().split('\n')

const n = Number(input[0])
graph = []

for (let i = 1; i < input.length; i++) {
  graph.push(input[i].split(''))
}

// 자리를 바꿀 2개의 사탕의 좌표 쌍을 전부 찾아라.
positions = []
for (let row = 0; row < n - 1; row++) {
  for (let col = 0; col < n - 1; col++) {
    positions.push([row, col, row + 1, col])
    positions.push([row, col, row, col + 1])
  }
}
for (let row = 0; row < n - 1; row++) {
  let col = n - 1
  positions.push([row, col, row + 1, col])
}
for (let col = 0; col < n - 1; col++) {
  let row = n - 1
  positions.push([row, col, row, col + 1])
}

// 자리를 바꾸고 행 체크, 열 체크
function swap(row1, col1, row2, col2) {
  let tmp = graph[row1][col1]
  graph[row1][col1] = graph[row2][col2]
  graph[row2][col2] = tmp
}

function rowCheck() {
  let maxSeries = 0
  for (let row = 0; row < n; row++) {
    let previous = graph[row][0]
    let cnt = 1
    for (let col = 1; col < n; col++) {
      if (previous == graph[row][col]) {
        cnt += 1
        if (col == n - 1) maxSeries = Math.max(maxSeries, cnt)
      } else {
        previous = graph[row][col]
        maxSeries = Math.max(maxSeries, cnt)
        cnt = 1
      }
    }
  }
  return maxSeries
}
function colCheck() {
  let maxSeries = 0
  for (let col = 0; col < n; col++) {
    let previous = graph[0][col]
    let cnt = 1
    for (let row = 1; row < n; row++) {
      if (previous == graph[row][col]) {
        cnt += 1
        if (row == n - 1) maxSeries = Math.max(maxSeries, cnt)
      } else {
        previous = graph[row][col]
        maxSeries = Math.max(maxSeries, cnt)
        cnt = 1
      }
    }
  }
  return maxSeries
}

let answer = 0
for (poss of positions) {
  swap(poss[0], poss[1], poss[2], poss[3])
  let curMax = Math.max(colCheck(), rowCheck())
  answer = Math.max(curMax, answer)
  swap(poss[0], poss[1], poss[2], poss[3])
}
console.log(answer)
