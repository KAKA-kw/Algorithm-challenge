var dictionary = []
var cadidate = ['A', 'E', 'I', 'O', 'U']

function dfs(str) {
  if (str.length > 5) return
  else if (str.length != 0) {
    dictionary.push(str)
  }

  for (char of cadidate) {
    dfs(str + char)
  }
}

function solution(word) {
  dfs('')
  dictionary.sort((a, b) => {
    for (i = 0; i < 5; i++) {
      if (a[i] != b[i]) return a[i] - b[i]
    }
  })
  return dictionary.indexOf(word) + 1
}
