class MinHeap {
  constructor() {
    this.heap = []
  }

  size() {
    return this.heap.length
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

  peek() {
    return this.heap[0]
  }

  // 값을 넣되, 오름차순 정렬함
  push(value) {
    this.heap.push(value)
    let currentIndex = this.heap.length - 1

    while (currentIndex > 0 && this.heap[currentIndex] < this.heap[this.parentIndex(currentIndex)]) {
      const temp = this.heap[currentIndex]
      this.heap[currentIndex] = this.heap[this.parentIndex(currentIndex)]
      this.heap[this.parentIndex(currentIndex)] = temp
      currentIndex = this.parentIndex(currentIndex)
    }
  }

  // 값을 빼되, 오름차순 정렬 함
  pop() {
    if (this.size() === 0) return null
    if (this.size() === 1) return this.heap.pop()

    const minValue = this.peek()
    this.heap[0] = this.heap.pop()
    let currentIndex = 0

    // 왼쪽 자식이 있다면
    while (this.heap[this.leftChildIndex(currentIndex)] !== undefined) {
      // 만약 오른쪽 자식 < 왼쪽 자식이라면
      // minChildIndex를 오른쪽 자식 인덱스로 할당, 그게 아니면 왼쪽 자식 인덱스를 할당

      // 먼저 오른쪽 자식이 있는지부터 검사하고 시작
      let minChildIndex =
        this.heap[this.rightChildIndex(currentIndex)] !== undefined && this.heap[this.rightChildIndex(currentIndex)] < this.heap[this.leftChildIndex(currentIndex)]
          ? this.rightChildIndex(currentIndex)
          : this.leftChildIndex(currentIndex)

      // 만약 자식이 더 크다면 멈춘다.
      if (this.heap[currentIndex] < this.heap[minChildIndex]) {
        break
      }

      // 만약 내가 더 크다면 자식보다 더 내려가야 함
      const temp = this.heap[currentIndex]
      this.heap[currentIndex] = this.heap[minChildIndex] // 더 큰 자식을 내 자리에 넣기
      this.heap[minChildIndex] = temp // 원래 자식 자리에는 나를 채워서 큰 내가 더 아래가도록
      currentIndex = minChildIndex
    }
    return minValue
  }
}

function solution(scoville, K) {
  const minHeap = new MinHeap()

  for (const sco of scoville) {
    minHeap.push(sco)
  }

  let mixedCount = 0

  while (minHeap.size() >= 2 && minHeap.peek() < K) {
    const first = minHeap.pop()
    const second = minHeap.pop()
    const mixedScov = first + second * 2
    minHeap.push(mixedScov)
    mixedCount++
  }

  return minHeap.peek() >= K ? mixedCount : -1
}
