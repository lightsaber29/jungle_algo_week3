s1 = [0] + list(input())
s2 = [0] + list(input())

len_1 = len(s1)
len_2 = len(s2)

lcs = [['' for _ in range(len_1)] for _ in range(len_2)]

for i in range(1, len_2):
    for j in range(1, len_1):
        if s1[j] == s2[i]:
            lcs[i][j] = lcs[i-1][j-1] + s1[j] #비교하는 숫자와 동일한 경우 왼쪽 대각선 위의 값 + 1
        else: #비교 문자와 다를 경우 
            if len(lcs[i][j-1]) > len(lcs[i-1][j]): #같은 행 길이가 더 클경우
                lcs[i][j] = lcs[i][j-1] #같은 행 문자 따름
            else: 
                lcs[i][j] = lcs[i-1][j] #같은 열 문자를 따름

answer = len(lcs[-1][-1])
print(answer)
if answer != 0:
    print(lcs[-1][-1])
