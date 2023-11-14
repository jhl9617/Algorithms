# https://www.acmicpc.net/problem/1241
# https://velog.io/@ddo_0/%EB%B0%B1%EC%A4%80-1241%EB%B2%88-%EB%A8%B8%EB%A6%AC-%ED%86%A1%ED%86%A1-by-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 머리 톡톡

import sys

t = 1000000
N = int(sys.stdin.readline())
circle = [int(sys.stdin.readline()) for _ in range(N)]
# list는 각 숫자가 몇 번 등장하는지 저장한다.
# 예를 들어 circle = [1,2,3,2]라면 list[1] = 1, list[2] = 2, list[3] = 1
list = [0]*(t+1)
# 저장
cnt = [0]*(t+1) 

# 각 원에 쓰여 있는 숫자를 센다.
for c in circle:
    list[c] += 1

for i in range(1,t+1):
    # 숫자 i가 있을 경우
    if list[i]:
        # 1을 뺀 것은 자기 자신을 제외하기 위함
        cnt[i] += list[i]-1 
        # 2*i, 3*i, 4*i, ... 는 i의 배수이므로 j의 cnt에 i 개수를 더해준다.
        for j in range(i+i,t+1,i): 
            cnt[j] += list[i]

answer = ""
for i in circle:
    answer += str(cnt[i]) + "\n"
print(answer)