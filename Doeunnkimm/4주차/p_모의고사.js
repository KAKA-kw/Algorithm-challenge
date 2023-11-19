function solution(answers) {
  const answer = []
  const first = [1, 2, 3, 4, 5]
  const second = [2, 1, 2, 3, 2, 4, 2, 5]
  const third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  const count = [0, 0, 0]

  for (let i = 0; i < answers.length; i++) {
    const ans = answers[i]
    if (first[i % first.length] === ans) count[0] += 1
    if (second[i % second.length] === ans) count[1] += 1
    if (third[i % third.length] === ans) count[2] += 1
  }
  const max = Math.max(count[0], count[1], count[2])

  if (count[0] === max) answer.push(1)
  if (count[1] === max) answer.push(2)
  if (count[2] === max) answer.push(3)

  return answer
}
