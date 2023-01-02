N = int(input())

num = list(map(int, input().split()))
num.sort()

for i in range(1, N+1):
    for j in range(2, N+1):
        if num[j] % num[i] == 0 and num[i] != 1:
            num[j] = num[j] // num[i]

print(num)
            # 3 4 2 

