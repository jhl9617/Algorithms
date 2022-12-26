a, b, c = map(int, input().split())


ea = 1
if c <= b:
    print("-1")
else:
    print(int(a / (c - b) + 1))
