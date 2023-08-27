# 그냥 dic을 사용하면 시간초과,,

# 접미사 배열(Suffix Array)을 사용

# 주어진 문자열 s에 대한 접미사 배열을 생성하는 함수
def build_suffix_array(s):
    n = len(s) # 문자열의 길이 저장
    sa = [0] * n  # 접미사 배열 저장
    group = [0] * n  # 그룹 정보 저장
    
    # 초기 단계: 글자 하나씩을 기준으로 정렬
    for i in range(n):
        sa[i] = i  # 접미사 배열 초기화
        group[i] = ord(s[i])  # 문자열을 아스키 코드로 변환하여 그룹 정보 초기화
    
    d = 1 # 기준이 되는 문자열의 개수 저장
    while d < n:
        # 두 개의 기준으로 정렬 (현재 그룹 정보와 d 위치 뒤의 그룹 정보)
        sa.sort(key=lambda x: (group[x], group[(x + d) % n]))
        
        new_group = [0] * n  # 새로운 그룹 정보를 저장할 리스트 초기화
        new_group[sa[0]] = 0  # 첫 번째 접미사는 항상 0번 그룹
        for i in range(1, n):
            # 이전 접미사와 현재 접미사의 그룹 정보가 같으면 같은 그룹, 아니면 다른 그룹
            if (group[sa[i]], group[(sa[i] + d) % n]) == (group[sa[i - 1]], group[(sa[i - 1] + d) % n]): # 튜플로 비교
                new_group[sa[i]] = new_group[sa[i - 1]] # 같은 그룹으로 설정
            else: # 다른 그룹으로 설정 
                new_group[sa[i]] = new_group[sa[i - 1]] + 1
        group = new_group
        d *= 2  # 기준을 2배씩 늘려가며 정렬
    
    return sa

# 최장 공통 접두사 배열(LCP 배열)을 생성하는 함수
def lcp_array(s, sa):
    n = len(s)
    rank = [0] * n  # 각 접미사의 순위 정보를 저장할 리스트
    lcp = [0] * n  # 최장 공통 접두사 배열 초기화
    
    for i in range(n):
        rank[sa[i]] = i  # 각 접미사의 순위를 저장
    
    k = 0 # 공통 접두사 길이를 저장할 변수
    for i in range(n):
        if rank[i] == n - 1:
            k = 0  # 만약 현재 접미사가 접미사 배열의 마지막이면 공통 접두사 길이는 0
            continue
        j = sa[rank[i] + 1]  # 다음 접미사의 인덱스
        while i + k < n and j + k < n and s[i + k] == s[j + k]: # 두 접미사의 공통 접두사를 찾음
            k += 1  # 공통 접두사 길이를 증가시킴
        lcp[rank[i]] = k
        if k > 0:
            k -= 1  # 공통 접두사 길이가 0보다 큰 경우 1 감소
    
    return lcp

# 최장 반복하는 부분 문자열의 길이를 계산하는 함수
def longest_repeating_substring(s):
    sa = build_suffix_array(s)  # 접미사 배열 생성
    lcp = lcp_array(s, sa)  # 최장 공통 접두사 배열 생성
    
    max_length = 0
    for length in lcp:
        max_length = max(max_length, length)  # 최장 공통 접두사 배열에서 가장 큰 값을 찾음
    
    return max_length

# 입력 받기
L = int(input())  # 문자열 길이 입력
string = input()  # 문자열 입력

# 결과 출력
result = longest_repeating_substring(string)  # 최장 반복 부분 문자열의 길이 계산
print(result)  # 결과 출력
