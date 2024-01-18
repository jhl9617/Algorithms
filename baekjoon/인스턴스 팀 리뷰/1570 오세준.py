# https://www.acmicpc.net/problem/1570
# https://oculis.tistory.com/174
# 오세준

def get_commands(n, sx, sy, ex, ey):
    ex -= sx
    ey -= sy

    if ex < 0 or ey < 0:
        return "-1"

    if ex == 0:
        return 'U' * min(ey, n) + 'R' * (n - min(ey, n))

    ans = set()

    for x in range(n, 0, -1):
        y = n - x       
        h = ex // x * y 

        if ey - y <= h <= ey + y:
            x1 = ex % x
            x2 = x - x1
            y1 = ey - h
            y2 = y - y1

            if x1 and y1 < 0:
                continue
            if not x1 and y1 < 0:
                y2 += y1
                y1 = 0

            ans.add('R' * x1 + 'U' * y1 + 'R' * x2 + 'U' * y2)

    if not ans:
        return "-1"

    return min(ans)

# -------------시작-----------------
n, sx, sy, ex, ey = map(int, input().split())

print(get_commands(n, sx, sy, ex, ey))
