# https://www.acmicpc.net/problem/10830

import sys

# 행렬 곱셈(제곱)
def multiple (A, curr):
    result = [[0 for _ in range(N)] for _ in range(N) ]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * curr[k][j]
            result[i][j] %= 1000
    return result

# 분할 정복
# curr 현재행렬, M 제곱수, A 초기행렬
def dnq(curr, M, A):
    if M == 1:
        return A
    elif M == 2:
        return multiple(A, A)
    else:
        temp = dnq(curr, M//2, A)
        if M % 2 == 0:
            return multiple(temp, temp)
        else:
            return multiple(multiple(temp, temp), A)


# 행렬 입력
N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
curr = A

result = dnq(curr, M, A)

for i in range (N):
    for j in range(N):
        print(result[i][j] % 1000, end=' ')
    print()
