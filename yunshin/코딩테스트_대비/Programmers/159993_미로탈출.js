const solution = (maps) => {
  const totRow = maps.length
  const totCol = maps[0].length
  const graph = maps.map((rows) => rows.split(''))

  const SXY = [0, 0]
  const EXY = [0, 0]
  const LXY = [0, 0]

  for (let row = 0; row < totRow; row++) {
    for (let col = 0; col < totCol; col++) {
      if (graph[row][col] === 'S') {
        SXY[0] = row
        SXY[1] = col
      }
      if (graph[row][col] === 'E') {
        EXY[0] = row
        EXY[1] = col
      }
      if (graph[row][col] === 'L') {
        LXY[0] = row
        LXY[1] = col
      }
    }
  }

  const bfs = (startXY, endXY) => {
    const que = [[...startXY, 0]]
    const visited = new Array(totRow).fill([]).map(() => new Array(totCol).fill(false))
    visited[startXY[0]][startXY[1]] = true
    const dx = [0, 0, -1, 1]
    const dy = [1, -1, 0, 0]

    while (que.length) {
      const [x, y, cost] = que.shift()
      if (x === endXY[0] && y === endXY[1]) {
        return cost
      }
      for (let i = 0; i < 4; i++) {
        const nx = dx[i] + x
        const ny = dy[i] + y
        if (0 <= nx && nx < totRow && 0 <= ny && ny < totCol && graph[nx][ny] !== 'X' && !visited[nx][ny]) {
          visited[nx][ny] = true
          que.push([nx, ny, cost + 1])
        }
      }
    }
    return -1
  }

  const SToL = bfs(SXY, LXY)
  const LToE = bfs(LXY, EXY)
  if (SToL == -1 || LToE == -1) return -1
  return SToL + LToE
}
