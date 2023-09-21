const input = require('fs').readFileSync('./input/b_10451.txt').toString().trim().split('\n')
const N = input[0]
const testArr = input.slice(1)

let map = []
let visited = []
let result = [] // 모든 테스트 케이스의 cycle 수를 한번에 담을 배열

function dfs(node) {
  visited[node] = true

  // 만약 node: 1 -> tail이면서 nextHead: 3
  // 3일 때 방문하지 않았다면, dfs
  const nextHead = map[node]
  if (!visited[nextHead]) {
    dfs(nextHead)
  }
}

for (let i = 0; i < N * 2; i += 2) {
  let cycle = 0
  map = [0, ...testArr[i + 1].split(' ').map(Number)] // 0번째짜리는 채워두기
  visited = Array(map.length).fill(false)

  // 순열이 10개라고 한다면
  // 위에서 인덱스0에 0을 채워넣어놓았기 때문에 map.length === 11이 될텐데
  // 순회는 인덱스 1부터 인덱스 10까지 돌면 되므로
  for (let j = 1; j < map.length; j++) {
    if (!visited[j]) {
      dfs(j)
      cycle++
    }
  }
  result.push(cycle)
}

console.log(result.join('\n'))
