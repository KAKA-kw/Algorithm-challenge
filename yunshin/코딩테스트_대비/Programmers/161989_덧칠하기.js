const solution = (n, m, section) => {
  const painted_wall = new Array(n + 1).fill(true)
  const first_ruin_idx = section[0]
  section.forEach((ruin) => {
    painted_wall[ruin] = false
  })
  let count = 0
  for (let i = first_ruin_idx; i < n + 1; i++) {
    if (painted_wall[i]) continue
    count++
    /* 벽 영역을 넘어갈 경우 */
    if (i + m >= n + 1) i = n + 1 - m
    for (let j = 0; j < m; j++) painted_wall[i + j] = true
  }
  return count
}
