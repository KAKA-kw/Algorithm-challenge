const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const T = +input.shift()
const each_cases = input.map((x) => +x)

// dp[1] 1,2,3 중 하나를 써서 만들 수 있는 수들의 집합
// dp[2] 1,2,3 중 두개(중복 가능)를 써서 만들 수 있는 수들의 집합

const dp = new Array(11)
dp[0] = []
dp[1] = [1, 2, 3]
for (let i = 2; i < 12; i++) {
  dp[i] = []
  for (const prev_val of dp[i - 1]) {
    for (let cur_val of [1, 2, 3]) {
      dp[i].push(prev_val + cur_val)
    }
  }
}

for (const number of each_cases) {
  let result = 0
  for (const dp_n of dp) {
    result += dp_n.filter((elem) => elem === number).length
  }
  console.log(result)
}
