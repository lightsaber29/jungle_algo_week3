# 5_9084 동전
# bottom-top 풀이

import sys
input = sys.stdin.readline

def get_number_of_cases(coins, price):
    print(f'get_number_of_cases :: coins: {coins} price: {price}')
    dp = [0]*(price+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, price + 1):
            dp[i] += dp[i - coin]
            print(dp)
    
    print(dp[price])

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().strip().split()))
    price = int(input())
    print(f'n: {n} coins: {coins} price: {price}')
    get_number_of_cases(coins, price)