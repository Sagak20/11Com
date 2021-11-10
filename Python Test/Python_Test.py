
""" # 2021 카카오 채용연계형 인턴십 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    index = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, num in enumerate(index):
        if num in s:
            s = s.replace(num, str(idx))
    answer = int(s)
    return answer

s1 = "one4seveneight"
s2 = "23four5six7"	
s3 = "2three45sixseven"	
s4 = "123"	

print(solution(s1)) #1478
print(solution(s2)) #234567
print(solution(s3)) #234567
print(solution(s4)) #123
"""

""" # 2021 카카오 블라인드 테스트 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = ""
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9\-\_\.]', '', answer)
    answer = re.sub('\.{2,}', '.', answer)
    answer = re.sub('^\.|\.$', '', answer)
    answer = 'a' if answer == '' else answer
    answer = answer[:15] if len(answer) > 15 else answer
    answer = re.sub('^\.|$\.', '', answer)
    while True:
        if len(answer) > 2:
            break
        answer = answer + answer[-1]
    return answer


id1 = "...!@BaT#*..y.abcdefghijklm"
id2 = "z-+.^."
id3 = "=.="
id4 = "123_.def"
id5 = "abcdefghijklmn.p"

print(solution(id1)) # "bat.y.abcdefghi"
print(solution(id2)) # "z--"
print(solution(id3)) # "aaa"
print(solution(id4)) # "123_.def"
print(solution(id5)) #"abcdefghijklmn"


# 1단계 대->소문자
# 2단계 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)이외 제거
# 3단계 마침표(.) 2번 이상 연속된 부분을 하나의 마침표(.)로 바꿈
# 4단계 첫, 끝 마침표(.) 제거
# 5단계 빈 문자열 = "a"
# 6단계 길이 >= 16자, 15개 외 제거 (제외 후 끝 (.)일 경우 제거)
# 7단계 길이 <= 2자, 길이 = 3 까지 마지막 문자 반복
"""