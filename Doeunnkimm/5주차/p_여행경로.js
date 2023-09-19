function solution(tickets) {
  const answer = []
  const visited = Array(tickets.length).fill(false)

  const DFS = (path) => {
    if (path.length === tickets.length + 1) {
      answer.push(path)
    } else {
      for (let i = 0; i < tickets.length; i++) {
        const [start, end] = tickets[i]
        if (!visited[i] && path.at(-1) === start) {
          visited[i] = true
          DFS([...path, end])
          // 다 돌면 다른 경우를 위해 false로 다시 초기화
          visited[i] = false
        }
      }
    }
  }
  DFS(['ICN'])
  // 가능한 경로가 2개 이상인 경우에 대해
  // 여러 경우가 담긴 2차원 배열에 대해 sort를 하게 되면
  // 알파벳 순으로 먼저 오는 경우로 먼저 정렬이 가능하다.
  return answer.sort()[0]
}
