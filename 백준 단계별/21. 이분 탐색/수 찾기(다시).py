import bisect

N = int(input())

num1 = map(int, input().split())
num1 = sorted(num1)

M = int(input())
num2 = map(int, input().split())

for i in num2:
    print("i : ", i)
    print(bisect.bisect(num1, i))
