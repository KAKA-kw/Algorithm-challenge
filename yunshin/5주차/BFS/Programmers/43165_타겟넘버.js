// BFS
function solution(numbers, target) {
  const Length = numbers.length
  const que = []
  let answer = 0
  let idx = 0
  que.push([numbers[idx], -numbers[idx]])
  idx += 1
  while (que.length !== 0) {
    let curNode = que.shift()
    if (idx === Length) {
      for (let cur of curNode) if (target == cur) answer += 1
    } else {
      let tempList = []
      for (let cur of curNode) {
        tempList.push(cur + numbers[idx])
        tempList.push(cur - numbers[idx])
      }
      que.push(tempList)
      idx += 1
    }
  }
  return answer
}
