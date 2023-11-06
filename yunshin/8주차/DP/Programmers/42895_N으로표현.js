function solution(N, number) {
  // dp[1] :  N 을 1개만 사용해서 나타낼 수 있는 array
  // dp[2] :  N 을 2개만 사용해서 나타낼 수 있는 array

  if (number === N) return 1
  const dp = Array.from(Array(9), () => [])
  dp[1].push(N)
  for (let i = 2; i < 9; i++) {
    const tmpSet = new Set()
    for (let j = 1; j < i; j++) {
      const k = i - j
      for (const jVal of dp[j]) {
        for (const kVal of dp[k]) {
          tmpSet.add(jVal + kVal)
          tmpSet.add(jVal * kVal)
          if (jVal > kVal) tmpSet.add(jVal - kVal)
          if (kVal > jVal) tmpSet.add(kVal - jVal)
          if (kVal && jVal % kVal === 0) tmpSet.add(jVal / kVal)
          if (jVal && kVal % jVal === 0) tmpSet.add(kVal / jVal)
        }
      }
    }
    tmpSet.add(+('' + N).repeat(i))
    if (Array.from(tmpSet).includes(number)) return i
    dp[i] = Array.from(tmpSet)
  }
  return -1
}
