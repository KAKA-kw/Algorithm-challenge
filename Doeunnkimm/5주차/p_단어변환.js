function solution(begin, target, words) {
  const visited = {[begin]: 0} // 방문하지 않았음: 0
  const queue = [begin]

  while (queue.length) {
    const current = queue.shift()
    if (current === target) break

    for (let word of words) {
      if (isConvertible(word, current) && !visited[word]) {
        visited[word] = visited[current] + 1
        queue.push(word)
      }
    }
  }
  return visited[target] || 0
}

// 한 단어만 다른지를 boolean으로 return 하는 함수
// 사용할 때 true를 반환해야만이 변환이 가능하다.
function isConvertible(str1, str2) {
  let count = 0

  for (let i = 0; i < str1.length; i++) {
    if (str1[i] !== str2[i]) count++
  }

  return count === 1
}
