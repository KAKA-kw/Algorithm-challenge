const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const [n, m] = input[0].split(' ').map((x) => +x)
const answer = []
const arr = []
const dfs = () => {
  if (arr.length === m) {
    answer.push([...arr])
    return
  }
  for (let i = 1; i <= n; i++) {
    arr.push(i)
    dfs()
    arr.pop()
  }
}
dfs()
console.log(answer.map((subArr) => subArr.join(' ')).join('\n'))
