const solution = (n) => {
  const stepsEachPosition = new Array(n + 1).fill(0)
  stepsEachPosition[1] = 1
  stepsEachPosition[2] = 2
  for (let i = 3; i < n + 1; i++) stepsEachPosition[i] = (stepsEachPosition[i - 1] + stepsEachPosition[i - 2]) % 1234567
  return stepsEachPosition[n]
}
