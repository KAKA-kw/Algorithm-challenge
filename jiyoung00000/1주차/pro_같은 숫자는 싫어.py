def solution(arr):
    ans = [arr[0]] # 결과를 저장할 리스트, 첫 번째 원소를 넣어줌.
    
    for i in range(1, len(arr)): # 두 번째 원소부터 순회. 연속적으로 같은 숫자를 건너뛰고 결과 리스트에 추가.
        if arr[i] != arr[i-1]: # 이전 원소와 현재 원소가 다르다면
            ans.append(arr[i]) # 결과 리스트에 현재 원소를 추가.
    
    return ans # 결과 리스트 반환