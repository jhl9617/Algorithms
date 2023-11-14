# https://www.acmicpc.net/problem/27940
# 가지 산사태

import sys
# ---------------시작---------------
N, M, K = map(int, sys.stdin.readline().split())

farms = [0] * (N + 1)

rains = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for i, (t, r) in enumerate(rains, start=1):
    # 해당 층에 빗물 더함
    for j in range(1, t + 1):
        farms[j] += r
        
        # 빗물의 양이 K를 초과
        if farms[j] > K:
            print(i, j)
            exit(0)

print(-1)

