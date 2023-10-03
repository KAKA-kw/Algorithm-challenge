function solution(tickets) {
  const srcToDes = {}
  const visited = {}
  const cities = new Set()
  for (const [src, des] of tickets) {
    cities.add(src)
    cities.add(des)
    if (!Object.keys(srcToDes).includes(src)) {
      srcToDes[src] = [des]
      visited[src] = [false]
    } else {
      srcToDes[src].push(des)
      visited[src].push(false)
    }
  }

  function check() {
    for (const city in visited) {
      for (const value of visited[city]) {
        if (!value) return false
      }
    }
    return true
  }
  const paths = []
  const answer = []
  function DFS(src) {
    if (check()) {
      answer.push([...paths])
      return
    }
    if (!srcToDes[src]) return
    srcToDes[src].forEach((dst, idx) => {
      if (!visited[src][idx]) {
        visited[src][idx] = true
        paths.push(dst)
        DFS(dst)
        visited[src][idx] = false
        paths.pop(dst)
      }
    })
  }
  paths.push('ICN')
  DFS('ICN')
  if (answer.length === 1) return answer[0]
  answer.sort()
  return answer[0]
}
