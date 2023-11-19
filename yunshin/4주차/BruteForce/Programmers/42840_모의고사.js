function solution(answers) {
  const supo1 = [1, 2, 3, 4, 5]
  const supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
  const supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

  let scores = [0, 0, 0]
  answers.forEach((val, idx) => {
    if (val == supo1[idx % supo1.length]) {
      scores[0] += 1
    }
    if (val == supo2[idx % supo2.length]) {
      scores[1] += 1
    }
    if (val == supo3[idx % supo3.length]) {
      scores[2] += 1
    }
  })
  let maxNum = Math.max(...scores)
  let answer = []
  scores.forEach((val, idx) => {
    if (val == maxNum) {
      answer.push(idx + 1)
    }
  })
  return answer
}
