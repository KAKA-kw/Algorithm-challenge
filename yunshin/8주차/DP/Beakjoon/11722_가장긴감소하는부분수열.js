const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const n = +input.shift()
const arr = input
  .shift()
  .split(' ')
  .map((x) => +x)

const dp = new Array(n).fill(1)
// dp[x] : 0 ~ x 까지의 가장 긴 감소하는 수열의 수
dp[0] = 1

for (let i = 1; i < n; i++) {
  for (let j = i - 1; j >= 0; j--) {
    if (arr[i] < arr[j]) dp[i] = Math.max(dp[i], dp[j] + 1)
  }
}

console.log(Math.max(...dp))
