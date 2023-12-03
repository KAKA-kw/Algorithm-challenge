function solution(money) {
  // dp[0].... 첫 집을 훔칠 경우
  // dp[1].... 첫 집은 봐줄 경우
  const numHouse = money.length
  const dp = Array.from(Array(2), () => new Array(numHouse).fill(0))

  dp[0][0] = dp[0][1] = money[0]
  dp[1][0] = 0
  dp[1][1] = money[1]

  for (let i = 2; i < numHouse - 1; i++) {
    dp[0][i] = Math.max(dp[0][i - 2] + money[i], dp[0][i - 1])
    dp[1][i] = Math.max(dp[1][i - 2] + money[i], dp[1][i - 1])
  }
  // 첫집을 훔친 경우라면, 마지막 집은 훔치면 안됨
  dp[0][numHouse - 1] = dp[0][numHouse - 2]
  dp[1][numHouse - 1] = Math.max(dp[1][numHouse - 1 - 2] + money[numHouse - 1], dp[1][numHouse - 1 - 1])

  const res_dp0 = dp[0][numHouse - 1]
  const res_dp1 = dp[1][numHouse - 1]
  return Math.max(res_dp0, res_dp1)
}
