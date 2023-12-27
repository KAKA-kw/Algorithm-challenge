// 최소스패닝트리
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [n, m] = input.shift().split(' ').map(Number)

const village = []
for (let i = 0; i < m; i++) {
  const [a, b, cost] = input[i].split(' ').map(Number)
  village.push({
    from: a,
    to: b,
    cost,
  })
}
village.sort((a, b) => {
  return a.cost - b.cost
})

const parent = new Array(n + 1).fill(0).map((_, idx) => idx)
const findParent = (x) => {
  if (x !== parent[x]) parent[x] = findParent(parent[x])
  return parent[x]
}
const union = (a, b) => {
  a = findParent(a)
  b = findParent(b)
  if (a < b) parent[b] = a
  else parent[a] = b
}
let totCost = 0
let maxCost = 0
village.forEach((item) => {
  const {from: a, to: b, cost} = item
  if (findParent(a) !== findParent(b)) {
    union(a, b)
    totCost += cost
    maxCost = Math.max(cost, maxCost)
  }
})

console.log(totCost - maxCost)
