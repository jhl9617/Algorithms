# https://www.acmicpc.net/problem/2740

import sys

# 행렬 A 입력
N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

# print(A) = [[1, 2], [3, 4], [5, 6]]

# 행렬 B 입력
M, K = map(int, sys.stdin.readline().split())
B = []
for i in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))

# print(B) = [[-1, -2, 0], [0, 0, 3]]

# K번 반복해서 한 행렬의 행과 다른 행렬의 열을 곱해서 더하고 출력
tmp = 0

# 행렬은 가로 N, 세로 K 크기로 output이 나옴
for i in range(N):
    for j in range(K):
        for k in range(M):
            tmp += A[i][k] * B[k][j]
        print(tmp, end=' ')
        tmp = 0
    print()