// BFS
function solution(begin, target, words) {
  const visited = new Array(words.length).fill(false)
  let answer = 0
  function getDiff(str1, str2) {
    let diff = 0
    for (let i = 0; i < str1.length; i++) {
      if (str1[i] != str2[i]) diff += 1
    }
    return diff
  }
  function BFS() {
    const que = []
    que.push([begin])
    while (que.length !== 0) {
      const curStrs = que.shift()
      const tempList = []
      for (let str of curStrs) {
        if (str === target) {
          return answer
        }
        for (let i = 0; i < words.length; i++) {
          if (!visited[i] && getDiff(str, words[i]) == 1) {
            visited[i] = true
            tempList.push(words[i])
          }
        }
      }
      if (tempList.length !== 0) {
        answer += 1
        que.push(tempList)
      }
    }
  }
  return BFS() || 0
}
