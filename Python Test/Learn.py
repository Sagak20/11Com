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

# 거스름돈
def GreedyPart1(): 
    n = 1260  # 거슬러줄 돈
    count = 0 # 동전 개수

    # 큰 단위 화폐부터 차례대로 확인
    coin_types = [500, 100, 50, 10]
    
    for coin in coin_types:
        count += n // coin # 나눈 몫, 거슬러 줄 동전 개수
        n %= coin          # 나눈 나머지, 1260 % 500 = 260
    print(count)

# 큰 수의 법칙
def GreedyPart2(): 
    # - 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
    # - 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것
    # - 배열의 크기 N, 숫자가 더해지는 횟수 M, K가 주어질 때의 결과를 출력하라
    # - 첫째줄 N, M, K 둘째줄 데이터
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

# 수학적 공식 이용한 효율적인 답안
def GreedyPart2_Answer1(): 
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
def GreedyPart3():
    # - 행렬 N x M
    # - 각 행의 최소값 중 최대값 선택
    # - 입력1 -> 2
    # 3 3
    # 3 1 2
    # 4 1 4
    # 2 2 2
    # - 입력2 -> 3
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
def GreedyPart4():
    # - N / K 가 나눠질 때만
    #   - N / K
    # - 나눠지지 않을 때
    #   - N - 1

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

"""#  구현
# 완전 탐색  : 모든 경우의 수를 주저 없이 다 계산 하는 해결 방법
# - 100만개 이하일 경우 유용
# 시뮬레이션 : 제시한 알고리즘을 한 단계씩 차례대로 직접 수행
# 데이터 개수(List길이)에 따른 메모리 사용량
#      1,000 - 약 4KB
#  1,000,000 - 약 4MB
# 10,000,000 - 약 40MB

# 상하좌우
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
        # 이동할 다음 좌표 구하기
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

# 시각(완전 탐색)
def implement_Part1_2(): 
    # 00시 00분 00초 ~ N시 59분 59초
    # 3이 포함된 모든 경우의 수
    # - 입력 -> 11475
    # 5
    # 경우의 수 = N x 60 x 60

    n = int(input())
    result = 0

    for h in range(n+1):        # 시
        for m in range(60):     # 분
            for s in ragne(60): # 초
                # 매 시각 3 포함일 경우
                if '3' in str(h) + str(m) + str(s):
                    result += 1

    return print(result)

# 왕실의 나이트
def implement_Part2():
    # 8x8 크기 체스판(a~h, 1~8)
    # 수평 2칸, 수직1칸 or 수직2칸, 수평1칸 이동 가능
    # 체스판 밖은 이동 불가
    # 입력값에 대한 이동 가능한 경우의 수 찾기
    # - 입력 -> 2
    # a2

    yx = input()
    x = int(yx[1])
    y = int(ord(yx[0])) - int(ord('a')) + 1
    # 이동 가능한 경우의 수
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    result = 0

    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            continue
        result += 1
    # 답안 예시
    # if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
    #   result += 1
    return print(result)

# 게임 개발
def implement_Part3():
    # 0(북), 1(동), 2(남), 3(서)
    # 맵 크기 N x M, 각각 육지(0) or 바다(1)
    # 미탐색 구역 이동
    # 1. 보는 방향 왼쪽 우선 탐색
    # 2. 왼쪽이 미탐색 - 좌회전 후 1칸 전진, 아니라면 좌회전 후 1단계
    # 3. 만약 4방향 모두 탐색 or 바다칸일 경우 - 1칸 후퇴 후 1단계
    #    후퇴 시 뒤가 바다면 정지 후 방문한 칸수 출력
    # - 입력 -> 3
    # 4 4     - 4 x 4 맵 생성
    # 1 1 0   - (1, 1) 0(북) 바라보는 캐릭터
    # 1 1 1 1 - 물, 물, 물, 물
    # 1 0 0 1 - 물, 땅, 땅, 물
    # 1 1 0 1 - 물, 물, 땅, 물
    # 1 1 1 1 - 물, 물, 물, 물

    n, m = map(int, input().split())
    x, y, direction = map(int, input().split())
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))
    
    # 가본 위치 저장
    chk = [[0] * m for _ in range(n)]
    # 시작 위치 탐색 처리
    chk[x][y] = 1

    # 방향에 따른 위치 이동
    stepx = [-1, 0, 1, 0]
    stepy = [0, 1, 0, -1]

    # 탐색 시작
    result = 1 # 결과
    turn = 0 # 탐색 횟수
    while True:
        # 왼쪽 회전
        direction -= 1
        if direction == -1:
            direction = 3

        nx = x + stepx[direction]
        ny = y + stepy[direction]

        # 미탐색일 경우
        if array[nx][ny] == 0 and chk[nx][ny] == 0:
            x = nx
            y = ny
            chk[x][y] = 1
            result += 1
            turn = 0
            continue
        # 탐색일 경우
        else:
            turn += 1
        # 4방향 탐색
        if turn == 4:
            nx = x - stepx[direction]
            ny = y - stepy[direction]
            # 뒤 이동 가능
            if array[nx][ny] == 0:
                x = nx
                y = ny
                turn = 0
                continue
            # 뒤 바다일 경우
            else:
                break
    return print(result)
"""

"""# 자료구조 기초
# - 탐색(Search) : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# - 자료구조(Data Structure) : 데이터를 표현하고 관리하고 처리하기 위한 구조
#   - 오버플로(Overflow) : 특정 자료구조의 데이터 크기가 가득찬 상태에서 삽입 연산을 할 때 발생
#   - 언더플로(Underflow) : 특정 자료구조의 데이터가 없는데 삭제 연산을 할 때 발생

# 스택(Stack) - 선입후출 First In Last Out
def Stack():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.pop()
    stack.append(4)
    stack.append(5)
    stack.pop()

    print(stack)       # 최하단 원소부터 출력
    # 1, 2, 4
    print(stack[::-1]) # 최상단 원소부터 출력
    # 4, 2, 1

# 큐(Queue) - 선입선출 First In First Out
from collections import deque
def Queue():
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.popleft()
    queue.append(4)
    queue.append(5)
    queue.popleft()
    
    print(queue)    # 먼저 들어온 순서대로 출력
    # 3, 4, 5
    queue.reverse() # 역순 정렬
    print(queue)    # 마지막 순서대로 출력
    # 5, 4, 3
    #리스트 자료형으로 사용 시
    list_queue = list(queue)

# 재귀함수(Recusive Function) - 자기자신 호출 함수
def Recusive_Function():
    print('재귀 함수 호출')
    Recusive_Function()

# 재귀함수 종료 조건, 10번 호출 시 종료
def Recusive_Function(i):
    if i == 10:
        return
    recursive_function(i + 1)
#Recusive_Function(1)
# -> 재귀함수는 스택 구조와 동일

# 팩토리얼(Factorial) - 재귀함수 대표 예제
# - n! = 1 x 2 x ... (n - 1) x n

# 반복문 구현
def factorial_iterative(n):
    result = 1
    # 1 ~ n 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀함수 구현
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 반환
        return 1
    # n! = n * (n - 1) 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 출력
#factorial_iterative(5) # 반복문 구현
#factorial_recursive(5) # 재귀함수 구현
"""

# DFS / BFS
# - 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프 연결 관계 표현
#   - 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
# - 인접 리스트(Adjacency list) : 리스트로 그래프 연결 관계 표현

# DFS(Depth-First Search) - 깊이 우선 탐색, 주로 스택
# - 데이터 개수 N개 -> O(N) 시간 소요

# 인접 행렬 예시
def Adjacency_Matrix():
    INF = 99999999
    graph = [[0, 7, 5],
             [7, 0, INF],
             [5, INF, 0] ]
    print(graph)

# 인접 리스트 예시
def Adjacency_List():
    # 행이 3개인 2차원 리스트로 인접 리스트 표현
    graph = [[] for _ in rage(3)]

    # 노드 0에 연결된 노드 정보 저장(노드, 거리)
    graph[0].append((1, 7))
    graph[0].append((2, 5))

    # 노드 1에 연결된 노드 정보 저장(노드, 거리)
    graph[1].append((0, 7))

    # 노드 2에 연결된 노드 정보 저장(노드, 거리)
    graph[2].append((0, 5))

    print(graph)

# 특징
# 메모리 사용 
# - 인접 행렬 : 노드간 모든 관계를 저장
#               노드 개수 많을수록 메모리 낭비
# - 리스트 행렬 : 연결된 노드만 저장
#                 특정한 두 노드 연결에 대한 정보 획득 속도가 느림

# DFS 예제
def DFS_ex():
    # DFS 메서드 정의
    def dfs(graph, v, visited):
        # 현재 노드를 방문 처리
        visited[v] = True
        print(v, end=' ')
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
    graph = [[],
             [2, 3, 8],
             [1, 7],
             [1, 4, 5],
             [3, 5],
             [3, 4],
             [7],
             [2, 6, 8],
             [1, 7]]

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
    visited = [False] * 9

    # 정의된 DFS 함수 호출
    dfs(graph, 1, visited)

# BFS(Breadth First Search) - 너비 우선 탐색, 주로 큐
# - 데이터 개수 N개 -> O(N) 시간 소요
# - deque 라이브러리 사용 추천
# - 실제 수행시간 빠르기 BFS > DFS 