function solution(m, n, puddles) {
  const dp = Array.from(Array(n + 1), () => new Array(m + 1).fill(0))

  dp[1][1] = 1 // 시작 위치에서 시작위치로 가는 경로는 단 하나!

  for (const [px, py] of puddles) {
    dp[py][px] = -1
  }

  for (let row = 1; row < n + 1; row++) {
    for (let col = 1; col < m + 1; col++) {
      // 위에서 했다.
      if (row === 1 && col === 1) {
        continue
      }
      // 웅덩이
      if (dp[+row][+col] == -1) {
        dp[row][col] = 0
        continue
      }
      // 가장 위쪽 가로줄
      if (row === 1) {
        dp[row][col] = dp[row][col - 1]
        continue
      }
      // 가장 왼쪽 세로줄
      if (col === 1) {
        dp[row][col] = dp[row - 1][col]
        continue
      }
      // 일반
      dp[row][col] += (dp[row - 1][col] + dp[row][col - 1]) % 1000000007
    }
  }
  return dp[n][m] % 1000000007
}
