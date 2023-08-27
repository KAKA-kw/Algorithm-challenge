const input = require('fs').readFileSync('b_2815.txt').toString().trim().split('\n')
const [C, R] = input

const cipher = C.split(' ')
const real = R.split(' ')

if (cipher.length === real.length) return console.log(1)

// $ 문자열 제거
cipher.pop()
real.pop()

// real 문자열을 맵 구조에 삽입
let i = 0
const charMap = new Map()
let realToNumString = ''

real.forEach((el) => {
  if (charMap.get(el) === undefined) {
    charMap.set(el, i)
    i++
  }
  realToNumString += charMap.get(el)
})

// cipher된 문자열을 돌면서 대조하기
let ans = 0
while (ans !== cipher.length - real.length) {
  // 맵 채우기
  let j = 0
  const cipherMap = new Map()

  for (let i = ans; i < cipher.length; i++) {
    if (cipherMap.get(cipher[i % cipher.length]) === undefined) {
      cipherMap.set(cipher[i], j)
      j++
    }
  }

  const cipherToNumString = cipher.map((ci) => cipherMap.get(ci)).join('')

  const index = cipherToNumString.indexOf(realToNumString)
  if (index < 0) {
    ans++
  } else {
    console.log(index + 1)
    break
  }
}
