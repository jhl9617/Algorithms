import sys

N = int(input())
num = []

for i in range(N):
    inp = sys.stdin.readline().split()

    if inp[0] == 'push':
        num.append(inp[1])
    elif inp[0] == 'pop':
        if num != []:
            print(num.pop())
        else:
            print(-1)
    elif inp[0] == 'size':
        print(len(num))
    elif inp[0] == 'empty':
        if num != []:
            print(0)
        else:
            print(1)
    elif inp[0] == 'top':
        if num != []:
            print(num[-1])
        else:
            print(-1)
