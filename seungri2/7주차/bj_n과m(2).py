n, m = list(map(int, input().split()))
s = []

def dfs(x):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    #순열 길이 = m이면 종류
    #for 루프에서 숫자 선택시, 이전에 선택한 숫자보다 크거나 같은 숫자만 고려 -> 중복 피하기
    #s에 포함되지 않은 숫자는 s에 추가
    for i in range(x, n+1):
        if i not in s:
            s.append(i)
            dfs(i + 1)
            s.pop()
    #호출 후 방금 추가한 숫자 s에서 제거
dfs(1)