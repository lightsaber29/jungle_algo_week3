# 4_2624 동전 바꿔주기
# bottom-top 풀이

import sys
input = sys.stdin.readline

t = int(input().strip())
k = int(input().strip())
penny = [list(map(int, input().strip().split())) for _ in range(k)]

dp = [0]*(t+1)
dp[0] = 1
for coin, count in penny:
    for price in range(t, 0, -1):
        for c in range(1, count+1):
            if price - coin*c >= 0:
                dp[price] += dp[price-coin*c]
                print(dp)
            else:
                break

print(dp[t])