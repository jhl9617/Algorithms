# https://www.acmicpc.net/problem/1461
# 도서관
import sys

n,m = map(int,input().split())
locations = list(map(int,input().split()))
pos = []
nag = []
locations.sort()

# 양수와 음수 분리
for i in locations:
    if i > 0:
        pos.append(i)
    else:
        nag.append(i)

# 마지막 책 m개의 위치
finalLocation = []

# 제인 먼 위치가 양수인지 음수인지 플래그
posOrNag = True
if abs(pos[-1]) > abs(nag[0]):
    # 가장 큰 수부터 m개 묶어서 이동
    finalLocation.append(pos[0:m])
    # pos[0:m] 원소 삭제
    del pos[0:m]
    
else:
    # 가장 작은 수부터 m개 묶어서 이동
    finalLocation.append(nag[0:m])
    del nag[0:m]
    posOrNag = False

# pos, nag 절대값이 큰게 앞으로 오도록 정렬
pos.sort(reverse=True)
nag.sort()

# 결과값
distance = 0

# 각 pos, nag의 원소들을 m개씩 묶어서 이동
for i in range(0,len(pos),m):
    distance += abs(pos[i])*2
for i in range(0,len(nag),m):
    distance += abs(nag[i])*2
    
# 마지막 책을 놓는 위치로 이동
if posOrNag:
    distance += finalLocation[0][-1]
else:
    distance -= finalLocation[0][0]

print(distance)