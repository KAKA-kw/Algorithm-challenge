function solution(sizes) {
  let maxWid = 0
  let maxHei = 0
  sizes.forEach((size) => {
    let [width, height] = size
    if (width > height) {
      maxWid = Math.max(maxWid, width)
      maxHei = Math.max(maxHei, height)
    } else {
      maxWid = Math.max(maxWid, height)
      maxHei = Math.max(maxHei, width)
    }
  })
  return maxWid * maxHei
}
