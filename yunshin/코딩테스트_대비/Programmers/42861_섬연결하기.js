// 최소스패닝트리
const solution = (n, costs) => {
  const parent = new Array(n).fill(0).map((_, idx) => idx)

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
  costs.sort((a, b) => a[2] - b[2])
  let answer = 0
  costs.forEach((path) => {
    const from = path[0]
    const to = path[1]
    const cost = path[2]
    if (findParent(from) !== findParent(to)) {
      union(from, to)
      answer += cost
    }
  })
  return answer
}
