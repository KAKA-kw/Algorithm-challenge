const input = require('fs').readFileSync('./input/b_2815.txt').toString().trim().split('\n')
const [cipher, real] = input

// 맨 끝 $ 문자열 제거, 공백을 기준으로 배열 생성
const cipher_arr = cipher.substring(0, cipher.length - 2).split(' ')
const real_arr = real.substring(0, real.length - 2).split(' ')

let index = 0
const map = new Map() // 사전 -> { key: 실제 단어, value: 암호화된 단어 }
let cipherString = ''

while (index !== cipher_arr.length - real_arr.length) {
  const temp = cipher_arr.slice(index, index + real_arr.length).join('')

  for (let i = 0; i < real_arr.length; i++) {
    const realToCipher = map.get(real_arr[i])
    if (realToCipher !== undefined && realToCipher !== temp[i]) {
      // 이미 사전에 있는데, 사전에 있는 단어와 실제 암호화된 단어와 다르다면 break
      break
    } else {
      // 사전에 없다면
      map.set(real_arr[i], temp[i])
      cipherString += temp[i]
    }

    if (cipherString === temp) {
      console.log(index + 1)
      return
    }
  }
  index++
  map.clear() // init
  cipherString = '' // init
}
