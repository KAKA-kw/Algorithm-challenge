# Heap (힙)

```
⭐️ 완전 이진 트리의 일종으로, 우선순위 큐를 위해 만들어진 자료구조
```

- 여러 개의 값들 중에서 **최댓값이나 최솟값을 빠르게 찾아내도록** 만들어진 자료구조
- Heap 트리에서는 중복된 값을 허용한다.
- 보틍 다른 언어의 경우에는 Heap 구조 자체를 기타 라이브러리를 통해 기본적으로 제공해주는 경우가 많다.
- JS는 없다.

> 물론, 코딩 테스트 영역 밖이라면 JS도 외부 라이브러리를 통해 heap을 사용할 수 있다.

## Heap의 종류

### 최대 힙 (max heap)

```
- 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
- key (부모 노드) >= key (자식 노드)
```

### 최소 힙 (min heap)

```
- 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진트리
- key (부모 노드) <= key (자식 노드)
```

<p align="center"><img src="https://gmlwjd9405.github.io/images/data-structure-heap/types-of-heap.png" /></p>

## Heap의 구현

- 힙을 저장하는 표준적인 자료구조는 **배열**이다.
- 힙의 경우 반정렬 상태(느슨한 정렬 상태)를 유지

  → 최대힙: 큰 값이 부모 노드쪽에 배치되도록 유지
  → 최소힙: 작은 값이 부모 노드쪽에 배치되도록 유지
  → 왼쫀 자식과 오른쪽 자식은 부모 노드보다 작은 값을 유지하기만!

- 배열의 첫 번째 값(index: 0)을 비워두는 경우가 종종 있다.

  이는 배열의 첫 번째 요소가 가지는 index는 0이기 때문에 1번째 라는 말과 인지부조화가 생기기에 계산의 편의성을 위해 그러는 경향을 띄는 편..

<p align="center"><img src="https://gmlwjd9405.github.io/images/data-structure-heap/heap-index-parent-child.png" width="70%"/></p>

- 자신: `N`
- 부모: `(N-1) / 2`
- 왼쪽 자식: `(N / 2) + 1`
- 오른쪽 자식: `(N / 2) + 2`

### 삽입

#### 최소힙에 데이터를 삽입하는 방법

<p align="center"><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtW3BE%2Fbtq0Vo0fs9A%2FPclulK9ZBBkhEhR76NUp9K%2Fimg.png" width="40%"/></p>

1. 저런 트리가 있다고 하자.
2. 1을 삽입하려고 할 때 완전이진트리의 요건을 만족시키기 위해 저 자리에 삽입
3. 자신의 값과 자신의 부모노드 값을 비교하여 자신의 값이 더 작으면 자리를 바꿈
4. 3번의 과정을 자신의 값이 부모노드 값보다 작을 때까지 혹은 루트에 도착할 때까지 반복한다.

```
⭐️ 이 작업은 밸런스가 맞춰져있는 완전이진트리에서 이루어지니까
   한 레벨씩 루트까지 올라간다면 한번 돌 때마다 절반씩 뚝뚝 떨어지므로
   O(log(n))의 시간복잡도를 갖는다.
```

### 삭제

#### 최소힙에서 최솟값 꺼내오기

<p align="center"><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcZdNHV%2Fbtq0Q8K6xJt%2FKOkH8iKUZp3SpuE9znJkMK%2Fimg.png"/></p>

1. 이런 최소힙이 있을 때, 최솟값은 당연히 루트에 있으므로 1을 가져온다.
2. 루트 자리가 비어버렸으니 채워야 한다. 완전이진트리의 **맨 마지막 노드를 가져온다.**
3. 가져오니까 정렬이 안 되어 있는 상태가 되므로, 자식 노드와 비교해서 자기보다 작은 노드와 자리를 바꾼다.
4. 내려와서 자기보다 작은 자식 5랑 자리를 바꾼다.
5. 이렇게 반복하다가 자식이 자기보다 크거나 리프노드에 도달하게 되면 멈춘다.

```
⭐️ 이 작업은 루트에서 한 레벨씩 내려가다가 맨 마지막 레벨까지 내려갈 수 있으니
최대 O(log(n))의 시간이 걸린다.
```

**👍 bubbleUp**

- 힙에 값을 삽입할 떄 부모와 비교해서 값이 크거나 작으면(`최소힙의 경우 부모가 자신보다 크면, 최대힙은 자신보다 작으면`) 부모와 값을 교환해서 올바르게 정렬이 될 때까지 올라가는 것을 편의상 bubbleUp이라고 한다.

**👍 bubbleDown**

- 힙에서 값을 꺼내올 때 아래 자식들과 비교해서 값이 크거나 작으면(`최소힙의 경우 자식이 자신보다 값이 작으면, 최대힙의 경우 자식이 자신보다 값이 크면`) 자식과 값을 교환해서 올바르게 정렬이 될 때까지 내려가는 것을 편의상 bubbleDown이라고 한다.

## 힙은 배열로 구현

- 배열의 인덱스는 각 항목의 차수/높이를 정의
- 첫 번째 배열 항목을 루트로 설정한 다음 각 왼쪽 항목과 오른쪽 항목을 순서대로 채움으로써 이진힙을 다룰 수 있음

```
다음 그림 속 힙의 경우 배열은 [2, 4, 23, 12, 13]
```

<p align="center"><img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbWfP8s%2Fbtq0Vo1xSpj%2Fu3rKtCk5anfLDtQP0siWkk%2Fimg.png" width="60%"/></p>

## 힙/최소힙/최대힙 구현코드

### 기본힙 (Heap)

```js
class Heap {
  constructor() {
    this.items = [] // 배열 생성
  }

  // 값을 서로 바꾸는 메서드
  swap(index1, index2) {
    let temp = this.items[index1]
    this.items[index1] = this.items[index2]
    this.items[index2] = temp
  }

  // 부모 인덱스 구하는 메서드
  parentIndex(index) {
    return Math.floor((index - 1) / 2)
  }

  // 왼쪽 자식 인덱스 구하는 메서드
  leftChildIndex(index) {
    return index * 2 + 1
  }

  // 오른쪽 노드 구하는 메서드
  rightChildIndex(index) {
    return index * 2 + 2
  }

  // 부모 노드 구하는 메서드
  parent(index) {
    return this.items[this.parentIndex(index)]
  }

  // 왼쪽 자식 노드 구하는 메서드
  leftChild(index) {
    return this.items[this.leftChildIndex(index)]
  }

  // 오른쪽 자식 노드 구하는 메서드
  rightChild(index) {
    return this.items[this.rightChildIndex(index)]
  }

  // 최대힙의 경우 최댓값을 반환하고 최소힙의 경우 최솟값을 반환하는 메서드
  peek() {
    return this.items[0]
  }
}
```

### 최소힙(MinHeap)

```js
class MinHeap extends Heap {
  // 부모 노드와 비교하면서 올리기
  bubbleUp() {
    let index = this.items.length - 1

    // 부모 노드가 존재하고, 부모 노드가 나보다 크다면 계속 반복
    while (this.parent(index) !== undefined && this.parent(index) > this.items[index]) {
      this.swap(index, this.parentIndex(index)) // 바꾸기
      index = this.parentIndex(index) // 현재 인덱스는 부모 노드 인덱스가 됨
    }
  }

  bubbleDown() {
    let index = 0

    // 내려갈 수 있고, 내가 왼쪽 자식 혹은 오르쪽 자식보다 작을 때까지 반복
    while ((this.leftChild(index) !== undefined && this.leftChild(index) < this.items[index]) || this.rightChild(index) < this.items[index]) {
      let smallerIndex = this.leftChildIndex(index)

      // 만약 오른쪽 자식이 있고, 오른쪽이 더 작다면
      if (this.rightChild(index) !== undefined && this.rightChild(index) < this.items[smallerIndex]) {
        smallerIndex = this.rightChildIndex(index)
      }

      this.swap(index, smallerIndex)
      index = smallerIndex
    }
  }

  // 힙에 원소를 추가하는 함수
  add(item) {
    this.items[this.items.length] = item
    this.bubbleUp()
  }

  // 힙에서 원소를 빼내는 함수
  // 최소 힙이라면 최솟값이 빠져나올 것이고 최대힙이라면 최댓값이 빠져나온다.
  poll() {
    let item = this.items[0] // 첫 번째 원소 keep
    this.items[0] = this.items[this.items.length - 1] // 맨 마지막 원소를 첫 번째 원소로 복사
    this.items.pop() // 맨 마지막 원소 삭제
    this.bubbleDown()

    return item // keep 해둔 값 반환
  }
}

class MaxHeap extends MinHeap {
  // MinHeap을 상속받되, bubbleUp과 bubbleDown을 재정의해보자

  bubbleUp() {
    let index = this.items.length - 1

    // 부모가 있는데, 내가 부모보다 크다면 반복
    while (this.parent(index) !== undefined && this.parent(index) < this.items[index]) {
      this.swap(index, this.parentIndex(index))
      index = this.parentIndex(index)
    }
  }

  bubbleDown() {
    let index = 0

    // 왼쪽 자식 노드가 존재하고, 내가 왼쪽 혹은 오른쪽 자식 노드보다 작다면 반복
    while ((this.leftChild(index) !== undefined && this.leftChild(index) > this.items[index]) || this.rightChild(index) > this.items[index]) {
      let largerIndex = this.leftChildIndex(index)

      if (this.rightChild(index) !== undefined && this.rightChild(index) > this.items[largerIndex]) {
        largerIndex = this.rightChildIndex(index)
      }

      this.swap(largerIndex, index)
      index = largerIndex
    }
  }
}
```
