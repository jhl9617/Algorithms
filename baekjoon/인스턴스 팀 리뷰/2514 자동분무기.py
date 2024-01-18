# https://www.acmicpc.net/problem/2514
# 자동분무기

import sys

# 기본 생산량 M과 분무기의 수 K를 입력받습니다.
M = int(sys.stdin.readline())  # 기본 생산량 M을 입력받습니다.
K = int(sys.stdin.readline())  # 분무기의 수 K를 입력받습니다.

# 농장의 생산량 데이터를 입력받습니다.
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(8)]  # 농장의 각 줄별 생산량을 입력받아 2차원 리스트로 저장합니다.

# 결과를 저장할 그리드를 초기화합니다.
result = [["." for _ in range(8)] for _ in range(8)]  # 8x8 격자를 '.'로 초기화합니다. '.'는 분무기가 없음을 나타냅니다.

# 실제 생산량과 기본 생산량의 차이를 계산하고, 행과 열의 합을 저장합니다.
adjusted = [[farm[i][j] - M for j in range(8)] for i in range(8)]  # 각 칸의 생산량에서 기본 생산량 M을 빼서 조정된 생산량을 계산합니다.
row_sums = [sum(adjusted[i]) for i in range(8)]  # 각 행의 조정된 생산량 합을 계산합니다.
col_sums = [sum(adjusted[i][j] for i in range(8)) for j in range(8)]  # 각 열의 조정된 생산량 합을 계산합니다.

# 분무기의 위치를 찾습니다.
for i in range(8):
    for j in range(8):
        # 행과 열의 합에서 해당 칸의 값을 뺀 값이 홀수이면 분무기가 있는 것으로 판단합니다.
        if (row_sums[i] + col_sums[j] - adjusted[i][j]) % 2 != 0:
            result[i][j] = '+'  # '+'는 비료 분무기가 있음을 나타냅니다.

# 각 분무기의 종류를 결정합니다.
for i in range(8):
    for j in range(8):
        if result[i][j] == '+':
            # 해당 칸을 포함한 행과 열에 있는 '+'의 수를 세어 분무기의 영향을 계산합니다.
            sprayer_effect = sum(result[i][k] == '+' for k in range(8)) + sum(result[k][j] == '+' for k in range(8)) - 1
            # 조정된 생산량 합과 분무기 영향의 차이를 통해 분무기의 종류를 결정합니다.
            if (row_sums[i] + col_sums[j] - adjusted[i][j] - sprayer_effect * 15) % 4 == 2:
                result[i][j] = '-'  # '-'는 제초제 분무기가 있음을 나타냅니다.

# 최종 결과를 출력합니다.
for row in result:
    print(' '.join(row))  # 각 줄을 출력합니다. '+'는 비료 분무기, '-'는 제초제 분무기, '.'는 분무기가 없음을 나타냅니다.