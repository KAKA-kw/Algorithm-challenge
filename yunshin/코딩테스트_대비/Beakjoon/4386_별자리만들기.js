// 최소스패닝트리
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input.shift())
const stars = []
for (let i = 0; i < N; i++) {
  stars.push(
    input
      .shift()
      .split(' ')
      .map((pos) => parseFloat(pos)),
  )
}
const getDistance = (pos1, pos2) => {
  return Math.pow(Math.pow(pos1[0] - pos2[0], 2) + Math.pow(pos1[1] - pos2[1], 2), 0.5)
}

const parent = new Array(N).fill().map((_, idx) => idx)
const findParent = (i) => {
  if (parent[i] !== i) {
    parent[i] = findParent(parent[i])
  }
  return parent[i]
}
const union = (a, b) => {
  a = findParent(a)
  b = findParent(b)
  if (a < b) parent[b] = a
  else parent[a] = b
}

const edges = []
for (let i = 0; i < N - 1; i++) {
  for (let j = i + 1; j < N; j++) {
    edges.push([getDistance(stars[i], stars[j]), i, j])
  }
}

edges.sort((arr1, arr2) => arr1[0] - arr2[0])

let answer = 0
edges.forEach((arr) => {
  const [cost, star1, star2] = arr
  if (findParent(star1) !== findParent(star2)) {
    union(star1, star2)
    answer += cost
  }
})
console.log(answer.toPrecision(3))
