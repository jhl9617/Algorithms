# https://www.acmicpc.net/problem/2740

import sys


def multiple (A):
    result = [[0 for _ in range(N)] for _ in range(N) ]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * A[k][j]
            result[i][j] %= 1000
    return result




# 행렬 입력
N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

print(A)
multiple(A)


# print(A) = [[1, 2], [3, 4], [5, 6]]

# 행렬은 가로 N, 세로 K 크기로 output이 나옴
