t = int(input())
for _ in range(t):
    H,W,N = map(int, input().split())
    a = N // H + 1
    b = N % H 
    if N % H == 0:
        a = N // H
        b = H
    
    a = format(a, '02')
    print(b, a, sep="")