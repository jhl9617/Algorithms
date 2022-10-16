import sys
input = sys.stdin.readline

x, y = map(int, input().split())

z = (y * 100) // x

count = 0
if z >= 99:print("-1")
else:
    while True:
        x += 1
        y += 1
        count += 1
        z2 = (y * 100) // x
        
        if z != z2:
            print(count)
            break

    

