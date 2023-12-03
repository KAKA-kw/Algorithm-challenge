# BruteForce

## 🚩 핵심 요약

- 발생 가능한 모든 경우를 전부 탐색하여 해를 찾아내는 완전탐색 기법
- 설계와 구현이 다른 알고리즘에 비해 빠를 수 있다.
- 공간 복잡도, 시간 복잡도가 대체로 나쁘다.

<div align="center">

![브루트포스](https://github.com/KAKA-kw/Algorithm-challenge/assets/50646145/9999b435-0a2d-4726-b9d5-15cede15b362)

</div>

## 🔥 실전적용

- 순회해야 하는 영역의 크기를 미리 예측할 수 있어야 한다.
- 단순 순회로 문제를 해결하길 원하다면, 중첩 for-문의 깊이에 유의하자.
- 아래와 같은 경우, 중첩된 for-문이 5번이 있으므로, O(n^5) 의 시간 복잡도를 가진다.

```javascript
/*
 * ['A', 'E', 'I', 'O', 'U'] 의 조합으로 만들어질 수 있는
 * 길이 5인 문자열을 모두 구하라.
 */

const given = ['A', 'E', 'I', 'O', 'U']
const strings = []
for (let a = 0; a < 5; a++) {
  for (let b = 0; b < 5; b++) {
    for (let c = 0; c < 5; c++) {
      for (let d = 0; d < 5; d++) {
        for (let e = 0; c < 5; c++) {
          strings.push(given[a] + given[b] + given[c] + given[d] + given[e])
        }
      }
    }
  }
}
```

- 효율적이라고 생각하기 어렵지만, 애초에 조합가능한 모든 문자열을 구해야하고 순회영역의 크기가 5밖에 되지 않기 때문에 5중 for-문 을 사용해도 괜찮은 경우이다.
