const input = require('fs').readFileSync('./input/b_1389.txt').toString().trim().split('\n')

const [N, M] = input[0].split(' ').map(Number)
const bacon = new Array(N + 1).fill(0) // 각 인덱스 자리에 베이컨 수를 채울 것 (0번 인덱스는 임의로 0으로 채워둠)
const graph = [...new Array(N + 1)].map(() => []) // 각 인덱스 자리에 관계가 있는 숫자를 채워넣을 것

// 각 사람 번호 자리에 관계가 있는 번호를 push
input.slice(1).forEach((v) => {
  let [start, end] = v.split(' ').map(Number)
  graph[start].push(end)
  graph[end].push(start)
})

const BFS = (start) => {
  const visited = new Array(N + 1).fill(false)
  const queue = [[start, 0]] // [node, 베이컨수]

  while (queue.length) {
    let [node, count] = queue.shift()

    // 만약 이미 방문한 node라면 push하는 과정 없이
    // 위에서 shift되고 queue를 비워나갈 것임
    if (!visited[node]) {
      visited[node] = true
      // 일단 queue에 관계가 있는 숫자들을 넣어놓고
      // shift되고 count를 세어야 하므로
      // count++을 통해 그 다음 숫자들부터 적용이 될 수 있도록
      bacon[start] += count++
      graph[node].forEach((v) => queue.push([v, count]))
    }
  }
}

for (let i = 1; i <= N; i++) {
  BFS(i)
}

bacon.shift() // 0번 인덱스에 존재하는 0 제거
console.log(bacon.indexOf(Math.min(...bacon)) + 1)
