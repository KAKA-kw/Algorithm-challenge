function solution(brown, yellow) {
  heightCandidate = []
  for (let h = 0; h < brown / 2; h++) if (2 * (brown + yellow) == (brown + 4 - 2 * h) * h) heightCandidate.push(h)
  if (heightCandidate.length == 1) return [heightCandidate[0], heightCandidate[0]]
  else return heightCandidate.sort((a, b) => b - a)
}
