const input = require('fs').readFileSync('./input/b_17413.txt').toString().trim()
let temp = []
let isTag = false
let ans = ''

for (let ch of input) {
  if (ch === '<') {
    ans += temp.join('')
    temp = [] // init
    isTag = true
    ans += ch
  } else if (ch === '>') {
    isTag = false
    ans += ch
  } else {
    if (isTag) {
      // 태그 안에 있는 텍스트일 경우
      ans += ch
    } else {
      if (ch === ' ') {
        // 태그 밖이긴 한데 공백일 경우
        ans += temp.join('') + ' '
        temp = [] // init
      } else {
        // 태그 밖에 있는 텍스트일 경우
        temp.unshift(ch)
      }
    }
  }
}

ans += temp.join('')

console.log(ans)
