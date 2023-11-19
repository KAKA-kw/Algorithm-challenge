function solution(brown, yellow) {
  let ans = 0
  const map = []

  for (let i = yellow; i > 0; i--) {
    if (yellow % i === 0) {
      const x = i
      const y = yellow / i
      if (x >= y) {
        map.push([x, y])
      } else {
        break
      }
    }
  }

  for (let [a, b] of map) {
    const b_x = a + 2
    const b_y = b

    if (b_x * 2 + b_y * 2 === brown) {
      ans = [b_x, b_y + 2]
      break
    }
  }
  return ans
}
