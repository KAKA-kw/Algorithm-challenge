const input = require('fs').readFileSync('./input/b_2178.txt').toString().trim().split('\n')

const [N, M] = input.shift().split(' ').map(Number)
const map = input.map((v) => v.split('').map(Number))
const [goalY, goalX] = [N - 1, M - 1] // 도착 위치

const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

// BFS
const bfs = (start) => {
  const queue = [[...start, 1]] // 좌표 및 움직인 칸 수

  while (queue.length) {
    const [curY, curX, move] = queue.shift()

    // 현재 위치가 도착 지점에 도달하면 움직인 칸 수 반환
    if (goalY === curY && goalX === curX) return move

    // 다음 이동할 4방향 탐색
    for (let i = 0; i < 4; i++) {
      const ny = curY + dx[i]
      const nx = curX + dy[i]

      // 다음 위치가 미로 밖으로 벗어나지 않고 길이 있는 곳(1)이면
      if (ny >= 0 && ny < N && nx >= 0 && nx < M && map[ny][nx]) {
        map[ny][nx] = 0 // 방문 처리
        queue.push([ny, nx, move + 1]) // 다음 위치넣고 한 칸 이동
      }
    }
  }
}

console.log(bfs([0, 0]))
