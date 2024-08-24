# 6_2294 동전
# bottom-top 풀이

import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
# 가치가 같은 동전이 여러 번 주어질 수도 있다 -> 중복 발생 가능성 제거를 위해 set 사용
coins = set(int(input().strip()) for _ in range(n))

dp = [10001] * (k+1)
# 여기서는 굳이 dp[0] = 1 처리를 할 필요가 없어서(최솟값을 찾아야 하니까) 0으로 세팅
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])