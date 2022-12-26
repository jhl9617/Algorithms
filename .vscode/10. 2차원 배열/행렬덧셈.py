N, M = map(int, input().split())

numa, numb = [], []

for i in range(N):
    i = list(map(int, input().split()))
    numa.append(i)

for i in range(N):
    i = list(map(int, input().split()))
    numb.append(i)

for i in range(N):
    for j in range(M):
        print(numa[i][j] + numb[i][j], end=' ')
    print()
