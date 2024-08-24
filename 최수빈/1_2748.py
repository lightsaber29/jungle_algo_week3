# 1_2748 피보나치 수
# bottom-top 풀이

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 91
# 초항 설정
dp[1] = 1
dp[2] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])