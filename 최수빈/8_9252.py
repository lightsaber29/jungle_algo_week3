# 8_9252 LCS2
# bottom-top 풀이

import sys
input = sys.stdin.readline

instr1 = [0] + list(input().strip())
instr2 = [0] + list(input().strip())

print(f'instr1: {instr1} instr2: {instr2}')

array = [['' for _ in range(len(instr1))] for _ in range(len(instr2))]

for i in range(1, len(instr2)): # CAPCAK
    for j in range(1, len(instr1)): # ACAYKP
        # 두 str이 동일할 때
        print(f'instr1[{j}]: {instr1[j]}, instr2[{i}]: {instr2[i]}')
        if instr1[j] == instr2[i]:
            print('same')
            array[i][j] = array[i-1][j-1] + instr1[j]
        else:
            # 값이 증가하기 전까지는 특정 구간동안? 값이 동일함...!
            if len(array[i][j-1]) > len(array[i-1][j]) :
                array[i][j] = array[i][j-1]
            else:
                array[i][j] = array[i-1][j]

for arr in array:
    print(arr)
answer = len(array[-1][-1])
print(answer)
if answer != 0 :
    print(array[-1][-1])
