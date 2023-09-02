const input = require('fs').readFileSync('./input/b_11279.txt').toString().trim().split('\n')

const testArr = input.slice(1)

class MaxHeap {
  constructor() {
    this.heap = []
  }
  swap(index1, index2) {
    const temp = this.heap[index1]
    this.heap[index1] = this.heap[index2]
    this.heap[index2] = temp
  }
  leftChildIndex(index) {
    return index * 2 + 1
  }
  rightChildIndex(index) {
    return index * 2 + 2
  }
  parentIndex(index) {
    return Math.floor((index - 1) / 2)
  }
  add(value) {
    this.heap.push(value)
    let currentIndex = this.heap.length - 1

    while (this.heap[this.parentIndex(currentIndex)] !== undefined && this.heap[this.parentIndex(currentIndex)] < this.heap[currentIndex]) {
      this.swap(this.parentIndex(currentIndex), currentIndex)
      currentIndex = this.parentIndex(currentIndex)
    }
  }
  extract() {
    if (this.heap.length === 0) return 0
    if (this.heap.length === 1) return this.heap.pop()

    const maxValue = this.heap[0]
    this.heap[0] = this.heap.pop()
    let currentIndex = 0

    while (this.heap[this.leftChildIndex(currentIndex)] !== undefined) {
      let maxChildIndex =
        this.heap[this.rightChildIndex(currentIndex)] !== undefined && this.heap[this.leftChildIndex(currentIndex)] < this.heap[this.rightChildIndex(currentIndex)]
          ? this.rightChildIndex(currentIndex)
          : this.leftChildIndex(currentIndex)

      if (this.heap[currentIndex] > this.heap[maxChildIndex]) break

      this.swap(currentIndex, maxChildIndex)
      currentIndex = maxChildIndex
    }
    return maxValue
  }
}

const heap = new MaxHeap()
const ans = []

testArr.forEach((el) => {
  if (el === '0') {
    ans.push(heap.extract())
  } else {
    heap.add(+el)
  }
})

console.log(ans.join('\n'))
