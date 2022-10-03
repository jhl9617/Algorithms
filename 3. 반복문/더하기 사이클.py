n = int(input())
if n < 10: n = n * 10
print("초기n : ", n)
tmp = n
cnt = 0

while True:
    a = tmp // 10
    print("a = ", a)
    b = tmp % 10
    print("b = ", b)
    c = (a + b) % 10
    print("c = ", c)
    tmp = (b * 10) + c
    print("tmp = ", tmp)
    cnt = cnt + 1
    print("cnt = ", cnt)
    if tmp == n:
        break
print(cnt)