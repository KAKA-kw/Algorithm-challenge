const solution = (people, limit) => {
  people.sort((a, b) => b - a)
  let boats = 0
  for (let i = 0, j = people.length - 1; i <= j; i++) {
    const weight_man = people[i]
    const light_man = people[j]
    if (weight_man + light_man <= limit) {
      j--
    }
    boats++
  }
  return boats
}
