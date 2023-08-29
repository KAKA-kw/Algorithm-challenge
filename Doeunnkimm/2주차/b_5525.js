const input = require('fs').readFileSync('b_5525.txt').toString().trim().split('\n')

let [N, M, S] = input
let answer = 0
let pattern = 0
let i = 0

while (i < M - 2) {
  if (S.slice(i, i + 3) === 'IOI') {
    pattern++
    if (pattern == N) {
      answer++
      pattern--
    }
    i += 2
  } else {
    pattern = 0
    i++
  }
}

console.log(answer)
