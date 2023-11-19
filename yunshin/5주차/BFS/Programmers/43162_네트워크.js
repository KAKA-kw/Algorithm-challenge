// BFS
function solution(n, computers) {
  const visited = new Array(n).fill(false)

  function BFS(startIdx) {
    const que = []
    que.push([startIdx])
    visited[startIdx] = true
    while (que.length !== 0) {
      let curIdxs = que.shift()
      let tmpList = []
      for (cur of curIdxs) {
        for (let nxt = 0; nxt < n; nxt++) {
          if (!visited[nxt] && computers[cur][nxt] === 1) {
            visited[nxt] = true
            tmpList.push(nxt)
          }
        }
      }
      if (tmpList.length !== 0) {
        que.push(tmpList)
      }
    }
  }
  let answer = 0
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      answer += 1
      BFS(i)
    }
  }
  return answer
}
