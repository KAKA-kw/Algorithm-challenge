const input = require('fs').readFileSync('./input/b_2583.txt').toString().trim().split('\n')

const [M, N, K] = input[0].split(' ').map(Number)
const coord = input.slice(1)
const paper = [...Array(M)].map(() => Array(N).fill(false)) // 존재하는 칸 수만큼 false를 채운 2차원 배열 생성

// 그려져있는 직사각형 자리는 true로 바꿔주기
for (let i = 0; i < K; i++) {
  const [x1, y1, x2, y2] = coord[i].split(' ').map(Number)
  for (let y = y1; y < y2; y++) {
    for (let x = x1; x < x2; x++) {
      paper[y][x] = true
    }
  }
}

const dx = [-1, 0, 1, 0]
const dy = [0, 1, 0, -1]

const dfs = (start) => {
  const queue = [start]
  let count = 0

  while (queue.length) {
    const [x, y] = queue.shift()
    count++

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      // 색칠 되지 않은 부분을 찾을건데, 이는 그려져있는 직사각형 이외의 위치이면서
      // 지금 방문하지 않은 곳을 찾아야하기 떄문에
      if (nx >= 0 && nx < M && ny >= 0 && ny < N && !paper[nx][ny]) {
        paper[nx][ny] = true
        queue.push([nx, ny])
      }
    }
  }
  return count
}

const areas = []
// 처음부터 끝까지 탐색
for (let i = 0; i < M; i++) {
  for (let j = 0; j < N; j++) {
    if (!paper[i][j]) {
      paper[i][j] = true
      areas.push(dfs([i, j]))
    }
  }
}

console.log(areas.length)
console.log(areas.sort((a, b) => a - b).join(' '))
