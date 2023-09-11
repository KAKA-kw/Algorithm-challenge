const input = require('fs').readFileSync('./input/b_3085.txt').toString().trim().split('\n')

const N = +input[0]
const candy = input.splice(1).map((v) => v.split('')) // e.g. [['C', 'C', 'P'], ['C', 'C', 'P']]

let max = 1

for (let i = 0; i < N; i++) {
  if (max == N) break
  for (let j = 0; j < N; j++) {
    if (max == N) break
    candySwap(i, j)
  }
}
console.log(max)

function candySwap(i, j) {
  const dir = [
    [0, 1],
    [1, 0],
  ]
  dir.forEach((v) => {
    const [x, y] = v

    // candy[i+x][j+y] !== candy[i][y] : 원래 사탕과 바꾸려는 사탕이 같을 경우에도 swap 하지 않음
    if (i + x > -1 && j + y > -1 && i + x < N && j + y < N && candy[i + x][j + y] != candy[i][j]) {
      let temp = candy[i][j]
      candy[i][j] = candy[i + x][j + y]
      candy[i + x][j + y] = temp
      checkRow()
      checkColumn()
      candy[i + x][j + y] = candy[i][j]
      candy[i][j] = temp
    }
  })
}

function checkRow() {
  for (let i = 0; i < N; i++) {
    let checkArr = [1]
    for (let j = 1; j < N; j++) {
      // 1번 인덱스부터 채워지게 됨
      // 바꿨을 때 같다면 이전 인덱스 +1 해서 넣는다. 그렇지 않다면 다시 1
      checkArr[j] = candy[i][j - 1] === candy[i][j] ? checkArr[j - 1] + 1 : 1
    }
    max = Math.max(...checkArr, max)
  }
}

function checkColumn() {
  for (let i = 0; i < N; i++) {
    let checkArr = [1]
    for (let j = 1; j < N; j++) {
      checkArr[j] = candy[j - 1][i] == candy[j][i] ? checkArr[j - 1] + 1 : 1
    }
    max = Math.max(...checkArr, max)
  }
}
