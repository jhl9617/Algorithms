from heapq import heappush, heappop,heapify
import sys

heap = []
N = int(sys.stdin.readline())

for i in range(N):
    a = int(sys.stdin.readline())
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, a)