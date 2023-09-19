function solution(maps) {
  const m = maps.length // 행 (y)
  const n = maps[0].length // 열 (x)
  const dy = [0, 0, 1, -1]
  const dx = [-1, 1, 0, 0]

  const queue = []
  queue.push([0, 0]) // 시작 좌표: (0, 0), 이동 칸 수: 1

  // 큐에 아이템이 있다면 반복
  while (queue.length) {
    const [curY, curX] = queue.shift()
    // 상대팀 진영 위치 (n-1, m-1)
    // 상대팀 진형에 도착하면 break
    if (curX === n - 1 && curY === m - 1) break

    // 상대팀 진영에 도착한 것이 아니라면
    for (let i = 0; i < 4; i++) {
      // 상하좌우 4방향에 대해서
      // 다음 위치를 결정
      const nx = curX + dx[i]
      const ny = curY + dy[i]

      // 다음 위치가 맵 내부이고 막힌 곳이 아니라면
      // 만약 여러 방향이 가능하더라도
      // 추후 가장 빠른 경로에서 바로 break된다.
      if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[ny][nx] === 1) {
        queue.push([ny, nx])
        // 다음 이동 거리 = 지금 이동 거리 + 1
        // 마지막에 상대방 진영 위치의 값이 결국 이동한 거리가 될 것임
        maps[ny][nx] = maps[curY][curX] + 1
      }
    }
  }
  return maps[maps.length - 1][maps[0].length - 1] === 1 ? -1 : maps[maps.length - 1][maps[0].length - 1]
}
