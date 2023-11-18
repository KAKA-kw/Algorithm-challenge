const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const N = +input.shift()
const stack = []

const answers = []
const push = (num) => {
  stack.push(num)
}
const pop = () => {
  if (stack.length == 0) answers.push(-1)
  else answers.push(stack.pop())
}
const size = () => {
  answers.push(stack.length)
}
const empty = () => {
  if (stack.length == 0) answers.push(1)
  else answers.push(0)
}
const top = () => {
  if (stack.length == 0) answers.push(-1)
  else answers.push(stack.at(-1))
}

for (let i = 0; i < N; i++) {
  const oper = input.shift().split(' ')
  if (oper[0] === 'push') push(+oper[1])
  if (oper[0] === 'pop') pop()
  if (oper[0] === 'top') top()
  if (oper[0] === 'empty') empty()
  if (oper[0] === 'size') size()
}

console.log(answers.join('\n'))
