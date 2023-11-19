var splited,
  numList = [],
  visited = []
var Composit = new Array(9999999 + 1).fill(false)

function dfs(curNum) {
  if (curNum != '') {
    numList.push(Number(curNum))
  }

  for (let i = 0; i < splited.length; i++) {
    if (!visited[i]) {
      visited[i] = true
      dfs(curNum + splited[i])
      visited[i] = false
    }
  }
}

// 에라토스테네스의 체
function isComposit() {
  Composit[0] = true
  Composit[1] = true

  for (let i = 2; i < Math.pow(Composit.length, 1 / 2); i++) {
    for (let j = 2; i * j < Composit.length; j++) {
      Composit[i * j] = true
    }
  }
}

function solution(numbers) {
  splited = numbers.split('')
  for (i = 0; i < splited.length; i++) {
    visited.push(false)
  }
  dfs('')
  numList = [...new Set(numList)]
  console.log(numList)
  isComposit()
  return numList.filter((x) => !Composit[x]).length
}
