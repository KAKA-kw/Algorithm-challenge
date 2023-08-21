# 큐(Queue)

- 데이터를 보관하는 선형 자료구조로, 데이터들이 일렬로 줄을 서 있는 형태.
- 큐는 데이터의 삽입(Enqueue)과 삭제(Dequeue)가 서로 다른 끝에서 이루어짐.
- 데이터를 추가할 때는 후단(Rear)에서 넣고, 데이터를 제거할 때는 전단(Front)에서 뺄 수 있다.

💡 queue: 줄을 서서 기다리다 > 데이터가 줄을 서서 대기하는 형태의 자료구조.

## 01 큐의 특징:

1. 선입선출(FIFO, First-In-First-Out) 원칙을 따릅니다. 가장 먼저 삽입된 데이터가 가장 먼저 삭제됨.
2. 큐에 데이터를 삽입하는 작업을 '인큐(Enqueue)'라고 하며, 데이터를 삭제하는 작업을 '디큐(Dequeue)'라고 함.
3. 큐의 전단(Front)에서 데이터가 제거되고, 후단(Rear)에서 데이터가 추가됨.

## 02 큐의 구현:

- 파이썬에서 리스트(List)를 활용하여 큐를 구현 가능. 리스트의 `append()` 메서드를 사용하여 데이터를 후단에 추가하고, `pop(0)` 메서드를 사용하여 데이터를 전단에서 삭제.

makefileCopy code

`queue = [] # 빈 큐 생성 # 데이터 인큐 queue.append(1)  queue.append(2)  queue.append(3)   # 데이터 디큐 dequeued_item = queue.pop(0) # 1이 디큐됨`

pythonCopy code

`class Queue:     def __init__(self):         self.queue = []      def enqueue(self, item):         self.queue.append(item)      def dequeue(self):         if not self.is_empty():             return self.queue.pop(0)         else:             print("큐가 비어있습니다.")      def front(self):         if not self.is_empty():             return self.queue[0]         else:             print("큐가 비어있습니다.")      def is_empty(self):         return len(self.queue) == 0      def size(self):         return len(self.queue)  # 큐 생성 my_queue = Queue()  # 데이터 인큐 my_queue.enqueue(1) my_queue.enqueue(2) my_queue.enqueue(3)  # 큐 크기 확인 print("큐 크기:", my_queue.size())  # 전단 데이터 확인 print("전단 데이터:", my_queue.front())  # 데이터 디큐 print("디큐한 데이터:", my_queue.dequeue()) print("디큐한 데이터:", my_queue.dequeue())  # 큐가 비어있는지 확인 print("큐가 비어있는지:", my_queue.is_empty())`

## 03 큐의 활용:

큐는 주로 다음과 같은 상황에서 활용됨.

- 자원 관리: 프로세스 스케줄링, 파일 및 네트워크 자원의 할당과 해제 등에서 큐를 활용하여 자원을 관리.
- 데이터 버퍼링: 데이터를 일시적으로 버퍼링하여 순서대로 처리할 때 큐를 활용.
- 너비 우선 탐색(Breadth-First Search, BFS): 그래프 탐색에서 큐를 사용하여 노드를 순서대로 방문.

## 04 큐의 시간 복잡도:

큐의 삽입과 삭제가 서로 다른 끝에서 이루어지지만, 시간복잡도는 모두 `O(1)`입니다.

- 데이터 인큐(`append`): O(1)
- 데이터 디큐(`pop(0)`): O(1)
- 전단 데이터 확인: O(1)

큐와 스택은 각각의 특징과 용도에 따라 다양한 상황에서 활용됩니다. 큐는 선입선출(FIFO)의 특성을 갖고 있어 대기열 관리와 순차적 처리가 필요한 경우에 유용하며, 스택은 후입선출(LIFO)의 특성을 가지고 있어 역순 처리와 재귀 알고리즘 등에 활용됩니다.
