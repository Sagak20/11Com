""" 주로 사용되는 입력 처리

list(map(int, input().split()))
 - split() : 입력 구분 문자
 - map(A, B)
   - A : 적용시킬 함수
   - B : 적용할 값들
   - 반환값 : map -> list형으로 변환하여 사용해야됨
줄바꿈 시
int(input())

대량 입력 시 입력 처리
import sys
data = sys.stdin.readline().rstrip()
 - rstrip() : 줄바꿈 공백 기호 제거
"""

""" 그리디(Greedy)

 - 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘
 - 나중에 미칠 영향에 대한 고려는 하지 않음
 - 떠올린 그리디 알고리즘이 정당한지 검토할 수 있어야 사용 가능
대표 문제
 - 거스름돈 : '가장 큰 화폐 단위부터' 거슬러 주는 것
"""
def GreedyPart1(): # 거스름돈
    n = 1260  # 거슬러줄 돈
    count = 0 # 동전 개수

    # 큰 단위 화폐부터 차례대로 확인
    coin_types = [500, 100, 50, 10]
    
    for coin in coin_types:
        count += n // coin # 나눈 몫, 거슬러 줄 동전 개수
        n %= coin          # 나눈 나머지, 1260 % 500 = 260
    print(count)

""" 큰 수 법칙
 - 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
 - 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것
 - 배열의 크기 N, 숫자가 더해지는 횟수 M, K가 주어질 때의 결과를 출력하라
 - 첫째줄 N, M, K 둘째줄 데이터
"""
def GreedyPart2(): # 큰 수의 법칙
    """
    - 입력
    5 8 3
    2 4 5 4 6
    - 출력 : 46   
    """
    n, m, k = map(int, input().split())
    N = list(map(int, input().split()))
    N.sort() # 입력 값 정렬
    first  = N[n-1] # 가장 큰 수
    second = N[n-2] # 다음 큰 수
    result = 0

    while True:
        for i in range(k):
            if m == 0: # M = 0 반복문 탈출
                break
            result += first
            m -= 1 
        if m == 0:
            break
        result += second
        m -= 1
    return print(result)

def GreedyPart2_Alt(): # 수학적 공식 이용한 효율적인 답안
    n, m, k = map(int, input().split())
    N = list(map(int, input().split()))
    N.sort() # 입력 값 정렬
    first  = N[n-1] # 가장 큰 수
    second = N[n-2] # 다음 큰 수

    # 가장 큰 수가 더해지는 횟수
    count  = int(m / (k + 1)) * k # 전체 크기 / ( 가장 큰 수 반복횟수 + 다음 수 ) * 반복 횟수
    count += m % (k + 1) # 반복 후 남은 가장 큰 수 개수

    result = 0
    result += (count) * first # 가장 큰 수 더하기
    result += (m - count) * second # 다음 큰 수 더하기

    return print(result)

""" 숫자 카드 게임
 - 행렬 N x M
 - 각 행의 최소값 중 최대값 선택
"""
def GreedyPart3(): # 숫자 카드 게임
    """
     - 입력1 -> 2
    3 3
    3 1 2
    4 1 4
    2 2 2
     - 입력2 -> 3
    2 4
    7 3 1 8
    3 3 3 4
    """
    n, m = map(int, input().split())
    result = 0

    for i in range(n):
        data = list(map(int, input().split()))
        imin = min(data) # 현재 행 작은 값
        result = max(result, imin)

    return print(result)
