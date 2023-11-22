const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})
const arr = []
rl.on('line', (input) => {
  arr.push(input.split(' ').map(Number))
})

rl.on('close', () => {
  const grade = arr[1]

  for (let i = 2; i < arr.length; i++) {
    const [s, e] = arr[i]
    const subRes = (grade.slice(s - 1, e).reduce((sum, add) => sum + add, 0) / (e - s + 1)).toFixed(2)
    console.log(subRes)
  }
  process.exit()
})
