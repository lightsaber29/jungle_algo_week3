n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

for i in range(3, n+1): #n이 3일 경우 3, n이 4일 경우 5라는 규칙이 있음
    dp[i] = (dp[i-1] + dp[i-2]) % 15746 #n이 최3ㅐ 1,000,000이므로 int의 범위를 넘어가는 경우가 있어서 중간중간 %15746을 해줘야 함
print(dp[n])
