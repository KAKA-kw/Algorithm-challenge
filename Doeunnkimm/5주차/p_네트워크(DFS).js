function solution(n, computers) {
  let visited = [false]
  let answer = 0

  function DFS(i) {
    visited[i] = true
    for (let j = 0; j < computers[i].length; j++) {
      if (computers[i][j] === 1 && !visited[j]) {
        DFS(j)
      }
    }
  }

  for (let i = 0; i < computers.length; i++) {
    if (!visited[i]) {
      DFS(i)
      answer++
    }
  }
  return answer
}
