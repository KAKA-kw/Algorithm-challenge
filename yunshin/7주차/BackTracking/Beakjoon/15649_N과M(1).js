const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [n, m] = input[0].split(' ').map((x) => +x)
const visited = new Array(n).fill(false)
const answerList = []
const subRes = []
const dfs = () => {
  if (subRes.length === m) {
    answerList.push([...subRes])
    return
  }
  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      visited[i] = true
      subRes.push(i + 1)
      dfs()
      subRes.pop()
      visited[i] = false
    }
  }
}
dfs()
const answer = answerList.map((val) => val.join(' '))
console.log(answer.join('\n'))
