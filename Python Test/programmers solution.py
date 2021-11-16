
# 키패드 누르기 - 2020 카카오 인턴십 
# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    Pad   = [[1,2,3], 
             [4,5,6], 
             [7,8,9], 
             ['*', 0,'#']]
    Left = 4



    answer = ''
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            Lnum = num
        elif num in [3, 6, 9]:
            answer += "R"
            Rnum = num
        elif num in [0, 2, 5, 8]:
            for i in range(4):
                for j in range(3):
                    if Pad[i][j]==num:
                        break
                    #좌표는 찾음, 비교해서 최단거리 체크
            #print(loc)
            answer += str(num)
    
    return answer

n1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
n2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
n3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(solution(n1, "right")) #"LRLLLRLLRRL"
print(solution(n2, "left"))  #"LRLLRRLLLRR"
print(solution(n3, "right")) #"LLRLLRLLRL"
change()

""" # 숫자 문자열과 영단어 - 2021 카카오 채용연계형 인턴십
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

