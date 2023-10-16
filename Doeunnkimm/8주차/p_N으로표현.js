function solution(N, number) {
  const use = Array.from(Array(9), () => new Set())

  if (N === number) return 1

  use.forEach((el, idx) => {
    if (idx !== 0) el.add(Number(String(N).repeat(idx)))
  })

  for (let i = 1; i <= 8; ++i) {
    for (let j = 1; j < i; ++j) {
      for (let first of use[j]) {
        for (let second of use[i - j]) {
          use[i].add(first + second)
          use[i].add(first - second)
          use[i].add(first * second)
          use[i].add(first / second)
        }
      }
    }
    if (use[i].has(number)) return i
  }
  return -1
}
