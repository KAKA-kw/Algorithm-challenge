function solution(prices) {
  let ans = []

  for (let i = 0; i < prices.length; i++) {
    let count = 0
    for (let j = 0; j < prices.length - i - 1; j++) {
      count++
      if (prices[i] > prices[i + j + 1]) {
        break
      }
    }
    ans.push(count)
  }
  return ans
}
