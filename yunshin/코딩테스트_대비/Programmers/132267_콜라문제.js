const solution = (a, b, n) => {
  let left = 0
  let in_hand = n
  let answer = 0

  while (in_hand !== 0) {
    in_hand += left
    const get_things = Math.floor(in_hand / a) * b
    left = in_hand % a
    in_hand = get_things
    answer += get_things
  }

  return answer
}
