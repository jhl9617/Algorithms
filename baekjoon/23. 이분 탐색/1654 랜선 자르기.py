# https://www.acmicpc.net/problem/1654
# 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lan:
        # mid 길이로 잘랐을 때 몇 개의 랜선이 나오는지
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)