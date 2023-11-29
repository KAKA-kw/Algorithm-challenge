const readline = require('readline')

;(async () => {
  const rl = readline.createInterface({input: process.stdin})

  let W = 0
  let N = 0
  let arr = []

  let inputCnt = 0

  for await (const line of rl) {
    if (N !== 0 && (inputCnt >= N || !line)) {
      rl.close()
    }

    if (!W) {
      ;[W, N] = line.split(' ').map(Number)
    } else if (arr.length < N) {
      arr.push(line.split(' ').map(Number))
    }
    inputCnt += 1
  }

  arr.sort((a, b) => b[1] - a[1])

  let totVal = 0
  for (const [wi, pi] of arr) {
    if (W >= wi) {
      totVal += wi * pi
      W -= wi
    } else {
      totVal += W * pi
      break
    }
  }

  console.log(totVal)

  process.exit()
})()
