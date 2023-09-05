const input = +require('fs').readFileSync('./input/b_2231.txt').toString().trim()

for (let i = 1; i <= input; i++) {
  const value = String(i)
    .split('')
    .map(Number)
    .reduce((acc, el) => acc + el, i) // i + 각 + 자 + 리 + 수 = input을 찾는다.

  if (value === input) {
    console.log(i)
    break
  }

  // 생성자가 없는 경우
  if (i === input) {
    console.log(0)
  }
}
