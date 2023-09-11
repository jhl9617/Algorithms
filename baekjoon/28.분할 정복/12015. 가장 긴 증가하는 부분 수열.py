# https://www.acmicpc.net/problem/12015

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# [10, 20, 10, 30, 20, 50]

dp = [arr[0]]
# dp = [10]

for i in range(1, n):
    # 현재 원소 arr[i]가 dp의 마지막 원소보다 큰 경우, 그냥 dp에 arr[i]를 추가
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        # arr[i]가 들어갈 위치를 이분 탐색
        
        dp[bisect_left(dp, arr[i])] = arr[i]

print(len(dp))

# bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# https://docs.python.org/ko/3/library/bisect.html
# 
# 10 20 10 30 20 50 의 경우
# 초기 dp = [10]
# 반복문에서는 20부터 시작
# 20은 dp의 마지막 원소보다 크므로 dp에 추가
# dp = [10, 20]
# 10은 dp의 마지막 원소보다 작으므로 dp[0] = 10을 10으로 바꿈
# dp = [10, 20]
# 30은 dp의 마지막 원소보다 크므로 dp에 추가
# dp = [10, 20, 30]
# 20은 dp의 마지막 원소보다 크므로 dp에 추가
# dp = [10, 20, 30, 50] 4개
# big(O) = nlogn