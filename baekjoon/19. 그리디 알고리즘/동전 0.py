N, K = map(int, input().split())
num = 0
list = []

for i in range(N):
    list.append(int(input()))

list.sort(reverse=True)

for i in list:
    if K / i > 0:
        num += (K // i)
        K = K % i

print(num)