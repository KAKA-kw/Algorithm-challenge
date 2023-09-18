// DFS
function solution(n, computers) {
  const visited = new Array(n).fill(false)

  function DFS(curIdx) {
    visited[curIdx] = true
    for (let nxtIdx = 0; nxtIdx < n; nxtIdx++) {
      if (!visited[nxtIdx] && computers[curIdx][nxtIdx] == 1) {
        DFS(nxtIdx)
      }
    }
  }
  let answer = 0
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      DFS(i)
      answer += 1
    }
  }
  return answer
}
