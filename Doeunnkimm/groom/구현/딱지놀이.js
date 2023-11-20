// Run by Node.js
const readline = require('readline')

;(async () => {
  let rl = readline.createInterface({input: process.stdin})

  const input = []
  for await (const line of rl) {
    input.push(line)
  }
  const N = input[0]
  const roundData = input.slice(1).map((state) => state.split(' ').map(Number))

  const winnerArray = [] // 각 라운드에서 A와 B 중 승자를 담을 배열 (무승부: D)

  for (let round = 0; round < N; round++) {
    const map = [
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ] // A와 B 정보를 담을 배열 (1~4 사용)
    const A = roundData[round * 2]
    const B = roundData[round * 2 + 1]

    A.slice(1).forEach((num) => (map[0][num] += 1))
    B.slice(1).forEach((num) => (map[1][num] += 1))

    // map을 검사
    const [aMap, bMap] = map
    for (let i = 0; i <= 3; i++) {
      if (aMap[4 - i] > bMap[4 - i]) {
        winnerArray.push('A')
        break
      }

      if (aMap[4 - i] < bMap[4 - i]) {
        winnerArray.push('B')
        break
      } else if (4 - i === 1) winnerArray.push('D') // 무승부인 경우
    }
  }

  console.log(winnerArray.join('\n'))

  // 문제의 오류로 마지막에 공백이 포함
  console.log('')

  process.exit()
})()
