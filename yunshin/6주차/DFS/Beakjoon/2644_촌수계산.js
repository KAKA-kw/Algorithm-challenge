// DFS
const input = require('fs').readFileSync('/dev.stdin').toString().trim().split('\n')
const n = +input.shift()
const [t1, t2] = input
  .shift()
  .split(' ')
  .map((x) => +x)
const m = +input.shift()
const graph = Array.from(Array(n + 1), () => new Array(n + 1).fill(0))
while (input.length) {
  const [parent, child] = input
    .shift()
    .split(' ')
    .map((x) => +x)
  graph[parent][child] = -1
  graph[child][parent] = -1
}

let answer = -1

const dfs = (cur, depth) => {
  if (cur === t2) {
    answer = depth
  }
  for (let i = 1; i < n + 1; i++) {
    if (graph[cur][i] === -1) {
      graph[cur][i] = depth + 1
      graph[i][cur] = depth + 1
      dfs(i, depth + 1)
    }
  }
}
dfs(t1, 0)
console.log(answer)
