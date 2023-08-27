def solution(phone_book): 
    # 전화번호를 해시에 저장
    phone_book_hash = {} 
    for number in phone_book:
        phone_book_hash[number] = True
    
    # 각 전화번호를 반복하면서 접두어인 경우를 확인
    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in phone_book_hash:
                return False
    
    return True