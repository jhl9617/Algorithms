# https://www.acmicpc.net/problem/2173
# 양파깡 만들기

from itertools import accumulate
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

#TODO: 누적합 
# 수평 누적합
hor_sum = [[0 for _ in range(N)] for _ in range(N)]
for row in range(N):
    hor_sum[row][0] = pan[row][0]
    for col in range(1, N):
        hor_sum[row][col] = hor_sum[row][col-1] + pan[row][col]
# 수직 누적합
ver_sum = [[0 for _ in range(N)] for _ in range(N)]
for col in range(N):
    ver_sum[0][col] = pan[0][col]
    for row in range(1, N):
        ver_sum[row][col] = ver_sum[row-1][col] + pan[row][col]

#TODO: 경우의수 생성, 위 아래 왼쪽 오른쪽 좌표 4개 저장
# 1, 3, 1, 3(위, 아래, 왼쪽, 오른쪽) 부터 8, 10, 8, 10까지 gang에 저장
gang = []
for top in range(N - 2):
    for left in range(N - 2):
        for bottom in range(top + 2, N):
            for right in range(left + 2, N):
                gang.append(( top + 1, bottom + 1, left + 1, right + 1))

#TODO:누적합으로 양파깡의 맛 계산
for i in gang:
    pass
#TODO: 양파깡의 맛을 기준으로 내림차순 정렬

result = []
#TODO: 제일 맛있는 양파깡 추출 후 해당 좌표 처리 하고 다음 추출. M번 반복


for i in result:
    print(i, sep=' ', end='\n')