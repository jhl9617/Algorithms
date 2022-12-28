
T = int(input())
for i in range(T):
    
    stack = []
    inp = input()
    for j in inp:
        brk = False
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack == []:
                brk = True
                break
            else:
                stack.pop()
    if stack == [] and brk == False:
        print('YES')
    else:
        print('NO')
