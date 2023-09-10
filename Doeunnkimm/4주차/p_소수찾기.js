function isPrime(num) {
  if (num <= 1 || (num > 2 && num % 2 === 0)) {
    return false
  }
  const sqrt = Math.sqrt(num)
  for (let i = 3; i <= sqrt; i += 2) {
    if (num % i === 0) {
      return false
    }
  }
  return true
}

function solution(numbers) {
  let count = 0
  const maxNum = +numbers
    .split('')
    .map(Number)
    .sort((a, b) => b - a)
    .join('')

  for (let i = 2; i <= maxNum; i++) {
    if (isPrime(i)) {
      let temp = 0 // 이게 i의 length만큼이 되어야만 count++
      const splitNums = numbers.split('')

      String(i)
        .split('')
        .forEach((n) => {
          const index = splitNums.indexOf(n) // ex. 17에서 1이 nums에 포함되는지 확인한다.

          if (index !== -1) {
            // 만약 있다면
            // 일단 있으므로 제거한다 (동일한 숫자를 다시 찾을 경우, 그때는 없다고 하기 위해)
            // ex. 17에서 11이 존재한다고 하는 경우를 제외하기 위해
            splitNums.splice(index, 1)
            temp++
          }

          // 소수의 모든 자리 숫자가 nums에 존재함을 확인했다면 count++
          if (temp === String(i).length) count++
        })
    }
  }
  return count
}
