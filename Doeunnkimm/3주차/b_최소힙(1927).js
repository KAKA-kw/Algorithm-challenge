const input = require('fs').readFileSync('./input/b_1927.txt').toString().trim().split('\n')

const testArr = input.slice(1)

class MinHeap {
  constructor() {
    this.heap = []
  }

  swap(index1, index2) {
    const temp = this.heap[index1]
    this.heap[index1] = this.heap[index2]
    this.heap[index2] = temp
  }

  parentIndex(index) {
    return Math.floor((index - 1) / 2)
  }

  leftChildIndex(index) {
    return index * 2 + 1
  }

  rightChildIndex(index) {
    return index * 2 + 2
  }

  add(value) {
    this.heap.push(value)
    let currentIndex = this.heap.length - 1

    while (currentIndex > 0 && this.heap[currentIndex] < this.heap[this.parentIndex(currentIndex)]) {
      this.swap(currentIndex, this.parentIndex(currentIndex))
      currentIndex = this.parentIndex(currentIndex)
    }
  }

  extract() {
    if (this.heap.length === 0) return 0
    if (this.heap.length === 1) return this.heap.pop()

    const minValue = this.heap[0]
    this.heap[0] = this.heap.pop()
    let currentIndex = 0

    while (this.heap[this.leftChildIndex(currentIndex)] !== undefined) {
      let minChildIndex =
        this.heap[this.rightChildIndex(currentIndex)] !== undefined && this.heap[this.rightChildIndex(currentIndex)] < this.heap[this.leftChildIndex(currentIndex)]
          ? this.rightChildIndex(currentIndex)
          : this.leftChildIndex(currentIndex)

      if (this.heap[currentIndex] < this.heap[minChildIndex]) break

      this.swap(currentIndex, minChildIndex)
      currentIndex = minChildIndex
    }
    return minValue
  }
}

const heap = new MinHeap()
const ans = []

testArr.forEach((el) => {
  if (el === '0') {
    ans.push(heap.extract())
  } else {
    heap.add(+el)
  }
})

console.log(ans.join('\n'))
