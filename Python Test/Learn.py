import time

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

""" 코드 시간 측정
import time
start = time.time()
end = time.time()
print(f"{end - start:.5f} sec")
"""

"""# 그리디(Greedy)
# - 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘
# - 나중에 미칠 영향에 대한 고려는 하지 않음
# - 떠올린 그리디 알고리즘이 정당한지 검토할 수 있어야 사용 가능
#대표 문제
# - 거스름돈 : '가장 큰 화폐 단위부터' 거슬러 주는 것
def GreedyPart1(): # 거스름돈
    n = 1260  # 거슬러줄 돈
    count = 0 # 동전 개수

    # 큰 단위 화폐부터 차례대로 확인
    coin_types = [500, 100, 50, 10]
    
    for coin in coin_types:
        count += n // coin # 나눈 몫, 거슬러 줄 동전 개수
        n %= coin          # 나눈 나머지, 1260 % 500 = 260
    print(count)

# 큰 수 법칙
# - 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# - 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것
# - 배열의 크기 N, 숫자가 더해지는 횟수 M, K가 주어질 때의 결과를 출력하라
# - 첫째줄 N, M, K 둘째줄 데이터
#
def GreedyPart2(): # 큰 수의 법칙
    # - 입력 -> 46
    # 5 8 3
    # 2 4 5 4 6
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

def GreedyPart2_Answer1(): # 수학적 공식 이용한 효율적인 답안
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

# 숫자 카드 게임
# - 행렬 N x M
# - 각 행의 최소값 중 최대값 선택
def GreedyPart3(): # 숫자 카드 게임
    #  - 입력1 -> 2
    # 3 3
    # 3 1 2
    # 4 1 4
    # 2 2 2
    #  - 입력2 -> 3
    # 2 4
    # 7 3 1 8
    # 3 3 3 4
    n, m = map(int, input().split())
    result = 0

    for i in range(n):
        data = list(map(int, input().split()))
        imin = min(data) # 현재 행 작은 값
        result = max(result, imin)

    return print(result)

# 1이 될 때까지
# - N / K 가 나눠질 때만
#   - N / K
# - 나눠지지 않을 때
#   - N - 1
def GreedyPart4():
    N, K = map(int, input().split())
    Count = 0

    while True:
        if N == 1:
            break
        elif N % K == 0 :
            Count += 1
            N = N // K
            continue
        else :
            Count += 1
            N = N - 1
    return print(Count)
def GreedyPart4_Answer1():
    n, k = map(int, input().split())
    result = 0

    while n >= k:
        # 나눠지지 않으면 1 빼기
        while n % k != 0: 
            n -= 1
            result += 1

        # 나눠지면 나누기
        n //= k # // 는 정수만 출력
        result += 1

    # 마지막 남은 수 1씩 빼기
    while n  > 1 :
        n -= 1
        result += 1

    return print(result)
def GreedyPart4_Answer2():
    # - 입력 -> 4
    # 27 5
    n, k = map(int, input().split())
    result = 0

    while True:
        # (N == K로 나누어 떨어지는 수)가 될때까지 1씩 빼기
        # N-27, K-5 
        target = (n // k) * k  # target은 25로 5의 배수인 나눠질 수
        result += (n - target) # n-target은 2로 -1씩 해야될 걸 한번에 계산함
        n = target # 바로 나눠질 수로 계산됨
        
        if n < k : # 반복문 탈출
            break
        # 나누기
        result += 1
        n //= k

    result += (n - 1) # 위 result += (n-target)에서 0
    return print(result)
"""

#  구현
# 완전 탐색  : 모든 경우의 수를 주저 없이 다 계산 하는 해결 방법
# 시뮬레이션 : 제시한 알고리즘을 한 단계씩 차례대로 직접 수행
# 데이터 개수(List길이)에 따른 메모리 사용량
#      1,000 - 약 4KB
#  1,000,000 - 약 4MB
# 10,000,000 - 약 40MB

def implement_Part1_1():
    # 크기 N x N (1, 1) ~ (N, N)
    # 방향 L(좌) R(우) U(상) D(하)
    # 시작점 (1, 1)
    #  - 입력 -> 3 4
    # 5           - 크기 N
    # R R R U D D - 이동 계획 plans
    # 맵 이탈 시 무시
    
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    # LRUD 이동방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    # 이동계획 확인
    for plan in plans :
        # 이동 후 좌표 구하기
        for i in range(len(move_types)): # 0, 1, 2, 3
            if plan == move_types[i] :
                nx = x + dx[i]
                ny = y + dy[i]
        # 맵 이탈 시 무시
        if nx < 1 or ny < 1 or nx > n or ny > n :
            continue
        # 이동
        x, y = nx, ny

    return print(x, y)
