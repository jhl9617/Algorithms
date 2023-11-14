# https://www.acmicpc.net/problem/2961
# 도영이가 만든 맛있는 음식

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
sour = []
bitter = []
for _ in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

diff = float('inf')

for i in range(1, n+1): # 재료를 i개 뽑을 때
    idxs = list(combinations(list(range(n)), i)) # 가능한 경우를 담은 리스트
    # idxs
    # [(0,), (1,), (2,), (3,)]
    # [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    # [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    # [(0, 1, 2, 3)]

    for food in idxs: 
        
        a = 1
        b = 0
        for j in range(i):
            a *= sour[food[j]]
            b += bitter[food[j]]
        if abs(a - b) < diff:
            diff = abs(a - b)

print(diff)