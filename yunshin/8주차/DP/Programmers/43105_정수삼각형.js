function solution(triangle) {
  const maxDepth = triangle[triangle.length - 1].length
  const graph = Array.from(new Array(maxDepth), () => new Array(maxDepth).fill(0))

  graph[0][0] = triangle[0][0]
  for (let row = 1; row < maxDepth; row++) {
    for (let col = 0; col <= row; col++) {
      let maxVal = 0
      if (col == 0) maxVal = Math.max(graph[row - 1][col])
      else if (col === row) maxVal = graph[row - 1][col - 1]
      else maxVal = Math.max(graph[row - 1][col - 1], graph[row - 1][col])
      graph[row][col] = triangle[row][col] + maxVal
    }
  }

  return Math.max(...graph[maxDepth - 1])
}
