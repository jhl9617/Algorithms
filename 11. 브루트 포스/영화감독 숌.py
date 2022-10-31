import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
tmp = 666
while cnt != n:
    if '666' in str(tmp):cnt += 1
    tmp += 1


print(tmp-1)