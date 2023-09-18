// DFS
function solution(numbers, target) {
  const Length = numbers.length
  let answer = 0
  const DFS = (acc, idx) => {
    if (idx === Length) {
      if (acc === target) answer += 1
      return
    } else {
      DFS(acc + numbers[idx], idx + 1)
      DFS(acc - numbers[idx], idx + 1)
    }
  }
  DFS(0, 0)
  return answer
}
