# sol 1
# n, k = map(int, input().split()) #n: 동전의 가지수, k: 목표 금액
# coins = [] # 동전 정보

# for _ in range(n):
#     coins.append(int(input()))

# dp = [100001 for i in range(k + 1)]
# dp[0] = 0

# for coin in coins:
#     for i in range(coin, k + 1):  # 현재 갖고 있는 동전 i를 기준으로 i 미만의 값은 갱신될리 없으므로 i부터 시작.
#         dp[i] = min(dp[i], dp[i - coin] + 1)

# if dp[k] == 100001:
#     print(-1)
# else:
#     print(dp[k])

#sol 2
n, k = map(int, input().split()) #n: 동전의 가지수, k: 목표 금액
coins = [] # 동전 정보

for _ in range(n):
    coins.append(int(input()))

dp = [100001 for i in range(k + 1)] # 동전의 개수가 아직 고려되지 않았다는 의미
dp[0] = 0 # 0원을 만들기 위해 필요한 동전의 개수(개수 측면)
#dp[0] = 1 # 0원은 아무 동전도 사용하지 않는 경우가 하나 있으므로 1으로 설정(경우의 수 측면)

for coin in coins:
    for i in range(coin, k + 1):  # 현재 갖고 있는 동전 i를 기준으로 i 미만의 값은 갱신될리 없으므로 i부터 시작.
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])
