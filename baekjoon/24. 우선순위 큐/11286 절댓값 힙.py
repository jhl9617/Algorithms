# https://www.acmicpc.net/problem/11286
# 절댓값 힙

from heapq import heappush, heappop
import sys
heap = []

N = int(sys.stdin.readline())

for i in range(N):
    inp = int(sys.stdin.readline())
    if inp == 0:
        if len(heap) > 0:
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap, (abs(inp), inp))
