# 스택(Stack)

- 데이터를 보관하는 선형 자료구조로, 데이터들이 한 줄로 나열된 형태.
- 데이터들은 스택의 맨 위에 있는 위치에만 삽입과 삭제가 가능.
- 즉, 데이터를 추가할 때는 항상 스택의 상단에 넣어야 하며, 데이터를 제거할 때도 항상 상단에서만 뺄 수 있다.

💡 stack: 쌓다 > 데이터를 차곡차곡 쌓아 올린 형태의 자료구조.

## 01 스택의 특징:

1. 후입선출(LIFO, Last-In-First-Out) 원칙을 따릅니다. 가장 나중에 삽입된 데이터가 가장 먼저 삭제됨.
2. 스택에 데이터를 삽입하는 작업을 '푸시(Push)'라고 하며, 데이터를 삭제하는 작업을 '팝(Pop)'이라고 함.
3. 가장 위쪽에 있는 데이터를 '탑(Top)'이라고 함.

## 02 스택의 구현:

- 파이썬에서 리스트(List)를 활용하여 스택을 구현 가능.
  리스트의 `append()` 메서드를 사용하여 데이터를 스택에 추가하고, `pop()` 메서드를 사용하여 데이터를 스택에서 삭제.

```
stack = [] # 빈 스택 생성
# 데이터 푸시
stack.append(1)
stack.append(2)
stack.append(3)

# 데이터 팝
popped_item = stack.pop() # 3이 팝됨
```

```
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("스택이 비어있습니다.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("스택이 비어있습니다.")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# 스택 생성
my_stack = Stack()

# 데이터 푸시
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# 스택 크기 확인
print("스택 크기:", my_stack.size())

# 탑 데이터 확인
print("탑 데이터:", my_stack.peek())

# 데이터 팝
print("팝한 데이터:", my_stack.pop())
print("팝한 데이터:", my_stack.pop())

# 스택이 비어있는지 확인
print("스택이 비어있는지:", my_stack.is_empty())

```

## 03 스택의 활용:

스택은 주로 다음과 같은 상황에서 활용됨.

- 함수 호출 및 재귀 알고리즘 구현: 함수 호출 정보를 스택에 저장하여 함수가 종료될 때 역순으로 호출 순서대로 처리.
- 수식 평가: 수식을 후위 표기법으로 변환하여 스택을 사용하여 연산을 수행.
- 뒤로가기 기능: 웹 브라우징에서 이전 페이지로 돌아가는 등의 기능을 스택을 통해 구현.

## 04 스택의 시간 복잡도:

스택의 삽입이나 삭제는 맨 위의 데이터를 바로 조작하기 때문에 시간복잡도는 늘 O(1)

- 데이터 푸시(`append`): O(1)
- 데이터 팝(`pop`): O(1)
- 탑 데이터 확인: O(1)

## 05 문제 풀이

1. [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586)
2. [프로세스](https://school.programmers.co.kr/learn/courses/30/lessons/42587)
3. [다리를 지나는 트럭](https://school.programmers.co.kr/learn/courses/30/lessons/42583)
