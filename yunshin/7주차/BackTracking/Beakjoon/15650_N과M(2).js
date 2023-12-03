const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const [n, m] = input
  .shift()
  .split(' ')
  .map((i) => +i)
const visited = new Array(n).fill(false)
const answer = []
const subRes = []
const isAscending = () => {
  for (let i = 1; i < subRes.length; i++) if (subRes[i - 1] > subRes[i]) return false
  return true
}
const dfs = (depth) => {
  if (subRes.length === m && isAscending()) {
    answer.push([...subRes])
    return
  }
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      visited[i] = true
      subRes.push(i + 1)
      dfs(depth + 1)
      subRes.pop()
      visited[i] = false
    }
  }
}
dfs()
console.log(answer.map((val) => val.join(' ')).join('\n'))
