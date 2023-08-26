// const input = require('fs').readFileSync('b_10256.txt').toString().trim().split('\n')
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

function getMarkerArray(marker) {
  const arr = []

  for (let i = 0; i < marker.length - 1; i++) {
    const a = marker[i + 1]
    const b = marker[i]

    const first = marker.substring(0, i)
    const third = marker.substring(i + 2, marker.length)
    arr.push(first + a + b + third)
  }

  for (let i = 0; i < marker.length - 2; i++) {
    const a = marker[i + 1] + marker[i + 2]
    const b = marker[i]

    const first = marker.substring(0, i)
    const third = marker.substring(i + 3, marker.length)
    arr.push(first + a + b + third)
  }

  for (let i = 3; i < marker.length; i++) {
    const a = marker[i]
    const b = marker[i - 1] + marker[i - 2]

    const first = marker.substring(0, i - 2)
    arr.push(first + a + b)
  }

  arr.push(marker.split('').reverse().join(''))
  arr.push(marker)
  return [...new Set(arr)]
}

function getMarkerInDNACount(DNA, markerMap) {
  let count = 0
  markerMap.forEach((marker) => {
    if (DNA.includes(marker)) count++
  })
  return count
}

function solution() {
  input.shift()
  var splitInput = []

  for (let i = 0; i < input.length; i += 3) {
    splitInput.push(input.slice(i, i + 3))
  }

  const sol = []
  splitInput.forEach((arr) => {
    const DNA = arr[1]
    const Marker = arr[2]
    sol.push(getMarkerInDNACount(DNA, getMarkerArray(Marker)))
  })
  console.log(sol.join('\n'))
}

solution()
