const input = require('fs').readFileSync('./input/b_10448.txt').toString().trim().split('\n').map(Number)
const testArr = input.slice(1)

// T_N 담기
const TN = [1] // 0번 인덱스 채우기 (의미없음)
for (let n = 1; n < 45; n++) {
  TN.push((n * (n + 1)) / 2)
}

// 자연수의 합이 1,000이 넘어가지 않기 때문에 n(n+1)/2=1000 -> n=45까지 삼각수를 구하면 된다.
function findTriangularNumber(n) {
  for (let i = 1; i < 45; i++) {
    for (let j = 1; j < 45; j++) {
      for (let k = 1; k < 45; k++) {
        if (TN[i] + TN[j] + TN[k] === n) {
          return 1
        }
      }
    }
  }
  return 0
}

function solution() {
  const ans = []
  testArr.forEach((n) => {
    ans.push(findTriangularNumber(n))
  })
  console.log(ans.join('\n'))
}

solution()
