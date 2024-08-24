import sys
input = sys.stdin.readline

# 사용한 추의 개수, num개의 추를 사용하여 만든 구슬의 무게
def cal(num, weight):
    # 사용할 수 있는 추의 개수를 넘어가면 종료
    if num > n:  return 
    # 1. num번째까지 추로 weight 무게를 만들 수 있음이 이미 기록되어있으면 종료
    if d[num][weight]:  return
    # 2. num번째까지 추로 weight 무게를 만들 수 있음을 체크
    d[num][weight] = True 
    
    # 3가지 경우 수행
    cal(num+1, weight + weights[num - 1]) #추를 오른쪽에 올리는 경우
    cal(num+1, weight - weights[num-1]) #추를 왼쪽에 올리는 경우
    cal(num+1, weight) #추를 사용하지 않는 경우
  
n = int(input())  # 추 개수
weights = list(map(int, input().split()))  # n개의 추의 무게
m = int(input())  # 구슬 개수
target = list(map(int, input().split()))  # m개의 구슬 무게
# d[i][j]: i번째까지 추를 사용했을 때 j무게를 만들 수 있는지 여부
d = [[False] * 15001 for _ in range(31)]

cal(0, 0)  # 지금까지 사용한 추 개수, 추로 만든 구슬의 무게를 0으로 시작

# m개의 구슬 무게를 확인할 수 있는지
for t in target:
    # 만들 수 있는 구슬의 무게는 30*500이 최대임
    if t > 15000:  print("N", end=" ") 
    elif d[n][t]: print("Y", end=" ")
    else:  print("N", end=" ")
