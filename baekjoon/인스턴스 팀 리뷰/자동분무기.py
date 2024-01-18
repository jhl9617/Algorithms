# https://www.acmicpc.net/problem/2514
# 자동분무기

import sys

M = int(sys.stdin.readline())
K = int(sys.stdin.readline())

farm = [list(map(int, sys.stdin.readline().split())) for _ in range(8)]

result = [["." for _ in range(8)] for _ in range(8)]


adjusted = [[farm[i][j] - M for j in range(8)] for i in range(8)]       #기본생산량 - M
row_sums = [sum(adjusted[i]) for i in range(8)]                         #각 행의 합
col_sums = [sum(adjusted[i][j] for i in range(8)) for j in range(8)]    #각 열의 합

# 분무기 위치 탐색
for i in range(8):
    for j in range(8):
       
        if (row_sums[i] + col_sums[j] - adjusted[i][j]) % 2 != 0:
            result[i][j] = '+'

# 분무기 종류 결정
for i in range(8):
    for j in range(8):
        if result[i][j] == '+':
           
            sprayer_effect = sum(result[i][k] == '+' for k in range(8)) + sum(result[k][j] == '+' for k in range(8)) - 1
           
            if (row_sums[i] + col_sums[j] - adjusted[i][j] - sprayer_effect * 15) % 4 == 2:
                result[i][j] = '-' 

for row in result:
    print(' '.join(row))