# https://www.acmicpc.net/problem/28353
# 28353번

import sys
N, K = map(int,sys.stdin.readline().split())
cats = []
happy = 0

cats = list(map(int,sys.stdin.readline().split()))  
cats.sort(reverse=True)

for i in range(N):
    for j in range(i+1,N):
        
        if cats[i] + cats[j] <= K:
            # print('행복해짐')

            # cats[i]와 cats[j]가 소모되고나서 중복되는 경우 방지
            cats[i] = K
            cats[j] = K
            happy += 1
            i += 1

print(happy)