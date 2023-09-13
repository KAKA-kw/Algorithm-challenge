// BFS
function solution(maps) {
  const totRow = maps.length
  const totCol = maps[0].length
  const dx = [1, -1, 0, 0]
  const dy = [0, 0, -1, 1]
  function BFS() {
    const que = []
    que.push([0, 0])
    while (que.length !== 0) {
      let [cx, cy] = que.shift()
      if (cx == totRow - 1 && cy == totCol - 1) {
        break
      }
      for (let i = 0; i < 4; i++) {
        let [nx, ny] = [cx + dx[i], cy + dy[i]]
        if (0 <= nx && nx < totRow && 0 <= ny && ny < totCol && maps[nx][ny] === 1) {
          maps[nx][ny] = maps[cx][cy] + 1
          que.push([nx, ny])
        }
      }
    }
  }
  BFS()
  let answer = maps[totRow - 1][totCol - 1]
  return answer !== 1 ? answer : -1
}
