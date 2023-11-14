# https://www.acmicpc.net/problem/21316
# 스피카

# --------시작--------
stars = [[] for _ in range(13)]
for _ in range(12):
    a, b = map(int, input().split())
    stars[a].append(b)
    stars[b].append(a)
# [[], [2], [1, 3], [2, 4, 7], [3, 5, 9], [4], [7], [3, 6, 8], [7, 9], [4, 8, 10], [9, 11], [10, 12], [11]]

for i in range(1, 13):
    if len(stars[i]) == 3:
        tmp = 0
        for j in stars[i]:
            tmp += len(stars[j] ) -1 
        if tmp == 3:
            print(i)
            break
# --------끝--------