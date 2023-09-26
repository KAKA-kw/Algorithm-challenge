// DFS
const input = require('fs')
  .readFileSync('/Users/yunshin/Documents/GitHub 오후 8.12.10/Algorithm-challenge/yunshin/6주차/DFS/Beakjoon/input/b_10451.txt')
  .toString()
  .trim()
  .split('\n')

const T = +input.shift()
let att = 0
const answer = []

while (att != T) {
  const n = +input.shift()
  const visited = new Array(n).fill(false)
  const arr = input
    .shift()
    .split(' ')
    .map((x) => +x)
  let result = 0

  const dfs = (idx) => {
    if (visited[idx]) {
      return
    }
    visited[idx] = true
    dfs(arr[idx] - 1)
  }

  arr.forEach((val, idx) => {
    if (!visited[idx]) {
      result++
      visited[idx] = true
      dfs(val - 1)
    }
  })
  answer.push(result)
  att++
}

console.log(answer.join('\n'))
