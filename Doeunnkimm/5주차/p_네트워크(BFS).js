function solution(n, computers) {
  let answer = 0
  const visited = []

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      answer++
      BFS(i)
    }
  }

  return answer

  function BFS(node) {
    visited[node] = true
    const q = [node]
    while (q.length !== 0) {
      const currentNode = q.shift()
      computers[currentNode].forEach((isConnected, nextNodeIndex) => {
        if (!isConnected || visited[nextNodeIndex]) return
        visited[nextNodeIndex] = true
        q.push(nextNodeIndex)
      })
    }
  }
}
