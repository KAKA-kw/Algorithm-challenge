const input = require('fs').readFileSync('./input/b_2309.txt').toString().trim().split('\n').map(Number)

const total = input.reduce((acc, el) => acc + el, 0)

let ans = ''

for (let i = 0; i < 9; i++) {
  if (ans.length > 0) break
  for (let j = i + 1; j < 9; j++) {
    if (total - input[i] - input[j] == 100) {
      ans = input
        .filter((_, k) => k != i && k != j)
        .sort((a, b) => a - b)
        .join('\n')
      console.log(ans)
      break
    }
  }
}
