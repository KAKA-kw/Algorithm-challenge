function solution(begin, target, words) {
  const visited = new Array(words.length).fill(false)
  let answer = 51
  function getDiff(str1, str2) {
    let diff = 0
    for (let i = 0; i < str1.length; i++) {
      if (str1[i] !== str2[i]) diff++
    }
    return diff
  }
  function DFS(curStr, depth) {
    if (curStr == target) {
      answer = Math.min(answer, depth)
      return
    }
    for (let i = 0; i < words.length; i++) {
      if (!visited[i] && getDiff(curStr, words[i]) === 1) {
        visited[i] = true
        DFS(words[i], depth + 1)
        visited[i] = false
      }
    }
  }
  DFS(begin, 0)
  return answer != 51 ? answer : 0
}
