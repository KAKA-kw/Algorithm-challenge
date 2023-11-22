const readline = require('readline')
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const inputs = []
rl.on('line', (line) => {
  inputs.push(line.split(' ').map(Number))
}).on('close', () => {
  const n = inputs[0]
  const stones = inputs[1]
  const dp = new Array(n).fill(0)
  for (let i = 0; i < n; i++) {
    let res = 0
    for (let j = 0; j < i; j++) {
      if (stones[j] < stones[i]) {
        res = Math.max(res, dp[j])
      }
    }
    dp[i] = res + 1
  }
  console.log(Math.max(...dp))
  process.exit()
})
