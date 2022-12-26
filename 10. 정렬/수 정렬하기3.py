import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())

numbers = [0]*10001

for i in range(n):
    numbers[int(input())] += 1
1
for i in range(1, 10001):
    for j in range(numbers[i]):
        print(str(i) + '\n')