const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const [n, m] = input[0].split(' ').map((x) => +x)
const answer = []
const arr = []
const isNonDescending = () => {
  let pre = arr[0]
  for (let i = 1; i < m; i++) {
    if (pre > arr[i]) {
      return false
    }
    pre = arr[i]
  }
  return true
}
const dfs = () => {
  if (arr.length > m) return
  if (arr.length == m && isNonDescending()) {
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
