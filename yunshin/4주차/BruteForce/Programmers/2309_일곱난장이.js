// DFS
const input = require('fs').readFileSync('dev/stdin').toString().trim().split('\n')
const visited = new Array(9).fill(false)

const result = []
function dfs(sumNum, depth) {
  if (depth == 7 && sumNum == 100 && result.length == 0) {
    for (let i = 0; i < 9; i++) if (visited[i]) result.push(Number(input[i]))
  }

  for (let i = 0; i < 9; i++) {
    if (!visited[i]) {
      visited[i] = true
      dfs(sumNum + Number(input[i]), depth + 1)
      visited[i] = false
    }
  }
}
dfs(0, 0)
result.sort((a, b) => a - b)
result.map((item) => {
  console.log(item)
})
