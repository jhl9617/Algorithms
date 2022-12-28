

n = int(input())
weight = []
height = []
numbers = []
for i in range(n):
    n, m = map(int, input().split())
    
    numbers.append((n, m))

for i in numbers:
    rank = 1
    for j in numbers:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end=" ")