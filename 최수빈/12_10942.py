import sys
input = sys.stdin.readline

# 팰린드롬 수가 중앙값 기준으로 앞, 뒤가 동일하다고 접근해서
# 앞에 있는 수를 스택에 쌓고 나머지를 for문으로 순회하면서 같은지 확인하려고 했는데 시간초과 발생
# def find_palindrome(num):
#     mid_idx = len(num)//2
#     stack = num[:mid_idx]
#     for i, n in enumerate(num[mid_idx+1:]):
#         if stack[i] != n:
#             return False
#     return True

# def find_palindrome(num):
#     mid_idx = len(num)//2
#     for i in range(mid_idx):
#         print(f'i: {i}')
#         if num[i] != num[len(num)-1]:
#             return False
#     return True

n = int(input())
nums = list(map(int, input().strip().split()))
m = int(input())
locates = [list(map(int, input().strip().split())) for _ in range(m)]

# 펠린드롬 수를 구성하는 숫자의 개수는 홀수 개 이다?
# 일단 이렇게 가정하고 중앙값을 찾아서 for 문 돌리기로 함

# for locate in locates:
#     a, b = locate
#     num = nums[a-1:b]
#     if len(num) == 1:
#         print(1)
#     elif len(num) == 2:
#         if num[0] == num[1]:
#             print(1)
#         else:
#             print(0)
#     else:
#         if find_palindrome(nums[a-1:b]):
#             print(1)
#         else:
#             print(0)

# 새 전략: 이차원 배열에 담기

# DP 배열 초기화
dp = [[False]*n for _ in range(n)]

# 길이가 1인 경우 (모든 수 자체는 팰린드롬)
for i in range(n):
    dp[i][i] = True

# 길이가 2인 경우 (연속된 두 수가 같으면 팰린드롬)
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = True

# 길이가 3 이상인 경우
for length in range(3, n+1):  # 길이 3부터 n까지
    for i in range(n-length+1):
        j = i+length-1
        if nums[i] == nums[j] and dp[i+1][j-1]:
            dp[i][j] = True

# 각 쿼리에 대해 결과 출력
for locate in locates:
    a, b = locate
    if dp[a-1][b-1]:
        print(1)
    else:
        print(0)