# Hash
from collections import defaultdict
def solution(phone_book):
    if len(phone_book) == 1:
        return True
    # 입력된 모든 전화번호의 길이를 저장
    lengths = set([len(phone) for phone in phone_book])
    # key - phone_book의 각 길이만큼의 앞부분 값
    # value - 같은 key 값을 가진 전화번호 갯수
    di = defaultdict(int)
    # 2중 for 문 최대 반복횟수: 10^6 X 20 = 2 X 10^7 (?)
    for phone in phone_book:
        for length in lengths:
            if len(phone) >= length:
                di[phone[:length]]+=1
    # 조건 1. key 값이 phone_book 에 있는 값이어야 한다.
    # 조건 2. value 가 2개 이상이어야 한다.
    for phone in phone_book:
        if di[phone] >= 2:
            return False
    return True