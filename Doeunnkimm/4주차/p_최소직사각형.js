function solution(sizes) {
  const rotated = sizes.map(([w, h]) => (w < h ? [h, w] : [w, h]))

  let maxW = 0
  let maxH = 0

  rotated.forEach(([w, h]) => {
    if (maxW < w) maxW = w
    if (maxH < h) maxH = h
  })

  return maxW * maxH
}
