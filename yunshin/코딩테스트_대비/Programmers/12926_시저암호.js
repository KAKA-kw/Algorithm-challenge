function solution(s, n) {
  const upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  const lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  const s_arr = s.split('')

  const result_arr = s_arr.map((char) => {
    if (upper.includes(char)) {
      let idx = upper.indexOf(char) + n
      return upper[idx % upper.length]
    }
    if (lower.includes(char)) {
      let idx = lower.indexOf(char) + n
      return lower[idx % lower.length]
    }
    return ' '
  })
  return result_arr.join('')
}
