function solution(s) {
  let stack = []
  s.split('').forEach((c) => {
    if (c === ')' && stack.includes('(')) {
      stack.pop()
    } else {
      stack.push(c)
    }
  })
  return stack.length === 0
}
