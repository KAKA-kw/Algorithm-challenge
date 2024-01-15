const solution = (k, d) => {
  let tot_count = 0
  for (let y = 0; y <= d; y += k) {
    const max_x = Math.floor(Math.sqrt(Math.pow(d, 2) - Math.pow(y, 2)))
    const x_count = Math.floor(max_x / k) + 1
    tot_count += x_count
  }
  return tot_count
}
