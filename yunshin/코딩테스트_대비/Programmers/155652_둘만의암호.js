const solution = (s, skip, index) => {
  const idx_to_alph = 'abcdefghijklmnopqrstuvwxyz'.split('')
  const alph_to_idx = {}
  idx_to_alph.forEach((char, idx) => {
    alph_to_idx[char] = idx
  })
  const answer = []
  s.split('').map((char, idx) => {
    let correct_idx = alph_to_idx[char]
    count = index
    while (count > 0) {
      correct_idx += 1
      if (correct_idx > 25) correct_idx = 0
      if (skip.includes(idx_to_alph[correct_idx])) count++
      count--
    }
    answer.push(idx_to_alph[correct_idx])
  })
  return answer.join('')
}
