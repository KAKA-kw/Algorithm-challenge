# 해시맵으로 푸는 방법 모르겠다!

# 세트를 사용하면 중복된 원소를 허용하지 않아서 시간 복잡도를 줄일 수 있음.

# 마커와 돌연변이를 생성하는 함수
def generate_mutations(marker):
    mutations = set()  # 중복된 돌연변이를 방지하기 위해 세트(set) 사용
    n = len(marker) # 마커의 길이 저장
    
    # 두 번째 부분을 뒤집는 모든 경우의 수 생성
    for i in range(n + 1):
        for j in range(n + 1):
            # 마커의 일부를 뒤집어 돌연변이를 생성
            mutated_marker = marker[:i] + marker[i:j][::-1] + marker[j:]
            mutations.add(mutated_marker)  # 생성된 돌연변이를 세트에 추가
    
    return mutations

# 주어진 DNA 구조에서 마커와 돌연변이가 몇 번 출현하는지 세는 함수
def count_mutations(dna, marker):
    mutations = generate_mutations(marker)  # 모든 돌연변이를 생성
    count = 0  # 출현 횟수를 저장할 변수를 초기화
    
    for i in range(len(dna) - len(marker) + 1):
        substring = dna[i:i + len(marker)]  # DNA 문자열에서 마커와 같은 길이의 부분 문자열을 추출
        if substring in mutations:  # 추출한 부분 문자열이 돌연변이 중에 있다면,
            count += 1  # 출현 횟수 증가
    
    return count

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # DNA 구조와 마커 입력
    n, m = map(int, input().split())  # n,m에 DNA 길이와 마커 길이 저장
    dna = input()  # dna에 DNA 문자열 저장
    marker = input()  # marker에 마커 저장
    
    # 결과 출력
    result = count_mutations(dna, marker)  # DNA에서 마커와 돌연변이가 몇 번 출현하는지 계산
    print(result)  # 결과를 출력
