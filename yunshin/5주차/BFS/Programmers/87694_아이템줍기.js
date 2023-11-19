function solution(rectangle, characterX, characterY, itemX, itemY) {
  const dx = [1, -1, 0, 0]
  const dy = [0, 0, -1, 1]
  const hx = [0.5, -0.5, 0, 0]
  const hy = [0, 0, -0.5, 0.5]
  const visited = new Array(51).fill().map((x) => Array(51).fill(false))

  function amIPath(x, y) {
    for (rect of rectangle) {
      let x1 = rect[0]
      let x2 = rect[2]
      let y1 = rect[1]
      let y2 = rect[3]
      // 완전 내부에 있으면 무조건 false
      if (x1 < x && x < x2 && y1 < y && y < y2) return false
      // 완전 외부에 있으면 무조건 false
      if (x < x1 && x2 < x && y < y1 && y2 < y) return false
    }
    for (rect of rectangle) {
      let x1 = rect[0]
      let x2 = rect[2]
      let y1 = rect[1]
      let y2 = rect[3]
      // x 좌표는 정확히 일치, y 좌표는 사이에 존재
      if ((x == x1 || x == x2) && y1 < y && y < y2) return true
      // y 좌표는 정확히 일치, x 좌표는 사이에 존재
      if ((y == y1 || y == y2) && x1 < x && x < x2) return true
      // 꼭지점
      if ((x == x1 || x == x2) && (y == y1 || y == y2)) return true
    }
    return false
  }

  function BFS() {
    que = []
    que.push([characterX, characterY, 0])
    visited[characterY][characterX] = true
    while (que.length !== 0) {
      const [curX, curY, cnt] = que.shift()
      if (curX == itemX && curY == itemY) {
        return cnt
      }
      for (let i = 0; i < 4; i++) {
        let [nxtX, nxtY] = [curX + dx[i], curY + dy[i]]
        if (0 <= nxtX && nxtX < 51 && 0 <= nxtY && nxtY < 51 && !visited[nxtY][nxtX] && amIPath(curX + hx[i], curY + hy[i])) {
          visited[nxtY][nxtX] = true
          que.push([nxtX, nxtY, cnt + 1])
        }
      }
    }
  }
  return BFS()
}
