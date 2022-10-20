t = int(input())
for _ in range(t):
    a = input()
    r = int(a[0])
    a = a[2:]
    result = []
    """print("t =", t,"a =", a, "r =",r, "result =", result)"""
    
    for i in a:
        for _ in range(r):
            result.append(i)
            
    print(*result, sep='')