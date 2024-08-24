# 3_9655 돌 게임
# bottom-top 풀이

# SK CY
# 1  1  => 2
# 1  3  => 4
# 3  1  => 4
# 3  3  => 6
# 매 턴마다 돌은 짝수 개 사라진다
# 따라서 홀수 개의 돌이 있다면 SK 승
# 짝수 개라면 CY 승 

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1001
# 초항 설정
dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4, n+1):
    dp[i] = (dp[i-1]+1) % 2

if dp[n] == 1:
    print('SK')
else:
    print('CY')