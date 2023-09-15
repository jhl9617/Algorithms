# https://www.acmicpc.net/problem/29156

import sys

N = int(sys.stdin.readline().rstrip())
tabs = []
for _ in range(N):
    tabs.append(int(sys.stdin.readline().rstrip()))

L = int(sys.stdin.readline().rstrip())
Q = int(sys.stdin.readline().rstrip())

clicks = []
current = 0
for _ in range(Q):
    clicks.append(int(sys.stdin.readline().rstrip()))

print(tabs)
print(current)
print(clicks)



print(tabs[current])


