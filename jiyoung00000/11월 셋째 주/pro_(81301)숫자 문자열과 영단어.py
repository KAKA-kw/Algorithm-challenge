def solution(s):
    words_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }  # 딕셔너리를 이용하여 숫자에 대응하는 영단어를 저장

    answer = ""  # 정답을 저장할 변수
    current_word = ""  # 현재 단어를 저장할 변수

    for char in s:  # 문자열을 하나씩 탐색
        if char.isalpha():  # 알파벳이면
            current_word += char  # 현재 단어에 추가
            if current_word in words_dict:  # 현재 단어가 딕셔너리에 있으면
                answer += words_dict[current_word]  # 정답에 추가
                current_word = ""  # 현재 단어 초기화
        else:  # 숫자면
            answer += char  # 정답에 추가

    return int(answer)  # 정수형으로 변환하여 반환
