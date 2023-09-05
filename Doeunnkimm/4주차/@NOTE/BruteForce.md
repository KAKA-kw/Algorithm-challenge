# BruteForce (부르트포스)

Brute: 무식한
Force: 힘

```
📌 복잡한 알고리즘을 굳이 생각하지 않고,
   컴퓨터의 빠른 연산력을 이용해 🔥모든 경우🔥를 다 살펴보는 것

   → brute force, BF, 완전 탐색이라고 불리기도 한다.
   → 대부분 반복문과 조건문을 통하여 답을 도출한다.
   → 모든 경우의 수를 전부 탐색하기 때문에 100% 정확성을 보장하지만,
     높은 시간 복잡도를 갖는다.
```

## 부르트포스 알고리즘 예신

### 1. 반복문을 사용하는 경우

```
비밀번호를 잊어버렸다면, 000부터 999까지 하나씩 돌리는 방식으로 비밀번호를 구할 수 있고,
자물쇠가 풀렸다면, 더는 돌릴 필요가 없다.
```

```js
const password = '345'

for (let i = 0; i < 10; i++) {
  for (let j = 0; j < 10; j++) {
    for (let k = 0; k < 10; k++) {
      if (String(i) + String(j) + String(k) === password) {
        console.log('풀렸습니다')
      }
    }
  }
}
```

### 2. 재귀를 사용하는 경우

```
10 팩토리얼을 구해라.
```

```js
function factorial(n) {
  if (n === 1) {
    return 1
  } else {
    return n * factorial(n - 1)
  }
}

console.log(factorial(10))
```
