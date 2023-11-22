const readline = require('readline')

;(async () => {
  const rl = readline.createInterface({input: process.stdin})

  let N = 0
  let M = 0
  let arr = []
  let relations = []
  let inputCnt = 1

  for await (const line of rl) {
    if (N !== 0 && inputCnt === M + 2) rl.close()

    if (!N) [N, M] = line.split(' ').map(Number)
    else if (!arr.length) arr = line.split(' ').map(Number)
    else relations.push(line.split(' ').map(Number))

    inputCnt++
  }
  const relationObj = {}
  for (const [p1, p2] of relations) {
    if (p1 in relationObj) {
      relationObj[p1].push(p2)
    } else {
      relationObj[p1] = [p2]
    }
  }
  const TFArray = new Array(N + 1).fill(true)
  for (const key in relationObj) {
    for (const val of relationObj[key]) {
      if (arr[key - 1] < arr[val - 1]) {
        TFArray[key] = false
      } else if (arr[key - 1] > arr[val - 1]) {
        TFArray[val] = false
      } else {
        TFArray[key] = false
        TFArray[val] = false
      }
    }
  }
  console.log(TFArray.filter((bool) => bool).length - 1)
  process.exit()
})()
