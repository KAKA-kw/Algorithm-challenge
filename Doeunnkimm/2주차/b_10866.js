const input = require('fs').readFileSync('./input/b_10866.txt').toString().trim().split('\n').slice(1)

const solution = (input) => {
  let deque = []
  let obj = {
    push_front: (val) => deque.unshift(val),
    push_back: (val) => deque.push(val),
    pop_front: () => deque.shift() || -1,
    pop_back: () => deque.pop() || -1,
    size: () => deque.length,
    empty: () => (deque.length === 0 ? 1 : 0),
    front: () => deque.at(0) || -1,
    back: () => deque.at(-1) || -1,
  }
  let result = []

  input.forEach((el) => {
    if (el.startsWith('pu')) {
      let [command, num] = el.split(' ')
      obj[command](num) // obj에서 함수를 찾아서 바로 실행
    } else {
      result.push(obj[el]())
    }
  })

  return result.join('\n')
}

console.log(solution(input))

/**
 * 📔 NOTE
 *
 * 문자열에서 어떤 특정 char을 포함되어 있는지 확인하고 싶다면
 * 무작정 includes를 사용하기 보다는, 만약 앞에 포함되는 것을 확신할 수 있다면 startsWith가 더 빠르다.
 */
