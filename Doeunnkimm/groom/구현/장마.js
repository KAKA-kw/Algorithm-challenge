// Run by Node.js
const readline = require('readline')

;(async () => {
  let rl = readline.createInterface({input: process.stdin})

  const input = []

  for await (const line of rl) {
    input.push(line)
  }

  const [N, M] = input[0].split(' ') // N: 집의 개수, M: 장마 기간
  const heights = input[1].split(' ').map(Number)
  const rainPosition = input.slice(2).map((p) => p.split(' ').map(Number))

  // 장마 시작
  const rainingSet = new Set() // 2일 이내에 비가 온 집을 기록
  rainPosition.forEach(([start, end], day) => {
    // start ~ end 위치의 집에 비가 내린다. -> 물의 높이 1 증가
    for (let i = start - 1; i < end; i++) {
      heights[i] += 1
      rainingSet.add(i)
    }

    // 배수 시스템 (3의 배수, 2일 이내에 비가 내린 위치에서만 작동)
    if ((day + 1) % 3 === 0) {
      ;[...rainingSet].forEach((i) => (heights[i] -= 1))
      rainingSet.clear() // 초기화
    }
  })

  console.log(heights.join(' '))
  process.exit()
})()
