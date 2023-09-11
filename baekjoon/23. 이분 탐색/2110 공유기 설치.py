# https://www.acmicpc.net/problem/2110

import sys 

N, C = map(int, sys.stdin.readline().split())
houses = []

for _ in range(N):
    houses.append(int(sys.stdin.readline()))

houses.sort()

# 최소 거리
start = 1
# 최대 거리
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    # 첫번째 집에 공유기를 설치
    value = houses[0]
    count = 1

    for i in range(1, N):
        # mid 보다 큰 값이 나오면 공유기를 설치
        if houses[i] >= value + mid:
            value = houses[i]
            count += 1

    # 공유기의 수가 C보다 크거나 같으면 거리를 늘림
    if count >= C:
        start = mid + 1
        result = mid
    # 공유기의 수가 C보다 작으면 거리를 줄임
    else:
        end = mid - 1
    
print(result)
