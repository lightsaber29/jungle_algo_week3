# 11_2629 양팔저울
# top-down 풀이

# 먼저 재귀로 돌면서 추로 만들 수 있는 무게의 dp 배열을 만듦
# 그리고 나중에 dp 배열에서 구슬에 해당하는 무게를 찾아 return

import sys
input = sys.stdin.readline

def recursive(num, weight):
    # 사용 가능한 추의 개수 초과 시 종료
    if num > n:
        return
    
    # 추로 무게를 만들 수 있는게 이미 기록되어있으면 종료
    if dp[num][weight]:
        return
    
    # num 개의 추로 무게를 만들 수 있으면 True 로 체크
    dp[num][weight] = True
    
    # 추를 놓는 3가지 경우의 수에 대해 탐색
    # 1. 추를 구슬과 같이 놓음
    recursive(num+1, weight+weights[num-1])
    # 2. 추를 구슬 반대편에 놓음
    recursive(num+1, abs(weight-weights[num-1]))
    # 3. 추를 놓지 않음
    recursive(num+1, weight)

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
beads = list(map(int, input().split()))
# 추의 개수에 따른 구슬의 무게 배열 생성 
dp = [[False] * 15001 for _ in range(31)]

recursive(0, 0)

# dp 배열에서 구슬 무게 확인
# 추의 최대 개수 30개, 최대 무게 500g -> 최대 측정가능 무게 = 30*500 = 15000
for bead in beads:
    if bead > 15000:
        print('N', end=' ')
    elif dp[n][bead]:
        print('Y', end=' ')
    else:
        print('N', end=' ')