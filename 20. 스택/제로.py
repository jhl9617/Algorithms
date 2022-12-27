K = int(input())
stack = []

for i in range(K):
    inp = int(input())
    if inp == 0:
        stack.pop()
    else:
        stack.append(inp)

tot = 0
for i in stack:
    tot += i
print(tot)
