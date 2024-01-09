const solution = (n, edge) => {
  const di = {}
  for (const [s, e] of edge) {
    di[s] = di[s] ? [...di[s], e] : [e]
    di[e] = di[e] ? [...di[e], s] : [s]
  }

  const distances = new Array(n + 1).fill(0).map((_) => Infinity)
  distances[0] = -1
  distances[1] = 0

  const heap = []
  heap.push([0, 1])

  const getMinWeiIdx = (arr) => {
    let minWei = Infinity
    let thatIdx = -1
    arr.forEach((elem, idx) => {
      const weight = elem[0]
      if (weight < minWei) {
        minWei = weight
        thatIdx = idx
      }
    })
    return thatIdx
  }

  while (heap.length) {
    const minWeightIdx = getMinWeiIdx(heap)
    const [curWei, curNod] = heap[minWeightIdx]
    heap.splice(minWeightIdx, 1)
    for (const nxtNod of di[curNod]) {
      if (1 + curWei < distances[nxtNod]) {
        distances[nxtNod] = 1 + curWei
        heap.push([1 + curWei, +nxtNod])
      }
    }
  }
  const maxWeight = Math.max(...distances)
  return distances.filter((elem) => elem == maxWeight).length
}
