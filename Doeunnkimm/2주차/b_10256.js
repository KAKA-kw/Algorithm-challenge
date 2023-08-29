const input = require('fs').readFileSync('./input/b_10256.txt').toString().trim().split('\n')

function getMarkerSet(marker) {
  const set = new Set()

  for (let i = 0; i <= marker.length; i++) {
    for (let j = 0; j <= marker.length; j++) {
      const reversed_second = marker.slice(i, j).split('').reverse().join('')
      set.add(marker.slice(0, i) + reversed_second + marker.slice(j))
    }
  }
  return set
}

function solution() {
  const test_count = input.shift()
  const case_arr = []

  // 테스트 케이스 구분
  for (let i = 0; i < input.length - 1; i += 3) {
    case_arr.push(input.slice(i + 1, i + 3))
  }

  // 테스트 케이스만큼 output 도출
  for (let i = 0; i < test_count; i++) {
    let count = 0
    const [dna, marker] = case_arr[i]
    const markerSet = getMarkerSet(marker)

    for (let j = 0; j < dna.length - marker.length + 1; j++) {
      if (markerSet.has(dna.slice(j, j + marker.length))) count++
    }
    console.log(count)
  }
}

solution()
