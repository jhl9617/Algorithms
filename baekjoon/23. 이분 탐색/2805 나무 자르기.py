# https://www.acmicpc.net/problem/2805
# 나무 자르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)
result = 0

while start <= end:
    mid = (end + start) // 2
    total = 0
    
    for i in tree:

        # 조건식이 없으면 마이너스도 더해짐
        if i > mid:
            total += i - mid # 잘린 나무의 길이를 더해줌
        
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)