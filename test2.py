# https://www.acmicpc.net/problem/1570
# 오세준

def osj():
    # 입력값을 받습니다. (명령의 길이, 시작 위치, 목표 위치)
    n, sx, sy, ex, ey = map(int, input().split())
    ex -= sx  # 목표 x 위치에서 시작 x 위치를 뺍니다.
    ey -= sy  # 목표 y 위치에서 시작 y 위치를 뺍니다.

    # 시작 위치가 목표 위치의 왼쪽이나 아래에 있는 경우, -1을 반환합니다.
    if ex < 0 or ey < 0:
        return "-1"

    # 오세준이 이미 지뢰와 같은 x축에 있는 경우, 오직 위로만 이동해야 합니다.
    if ex == 0:
        return 'U' * min(ey, n) + 'R' * (n - min(ey, n))

    # 가능한 경로를 저장할 집합을 초기화합니다.
    ans = set()

    # 명령의 조합을 탐색합니다.
    for x in range(n, 0, -1):
        y = n - x  # 오른쪽으로 이동할 횟수
        h = ex // x * y  # 현재 x, y 조합으로 이동했을 때의 높이

        # 지뢰에 도달할 수 있는지 확인합니다.
        if ey - y <= h <= ey + y:
            x1 = ex % x  # 오른쪽으로 남은 이동 횟수
            x2 = x - x1  # 나머지 오른쪽 이동 횟수
            y1 = ey - h  # 위로 남은 이동 횟수
            y2 = y - y1  # 나머지 위로 이동 횟수

            # 이동 불가능한 조건을 확인하고 건너뜁니다.
            if x1 and y1 < 0:
                continue
            if not x1 and y1 < 0:
                y2 += y1
                y1 = 0

            # 가능한 경로를 집합에 추가합니다.
            ans.add('R' * x1 + 'U' * y1 + 'R' * x2 + 'U' * y2)

    # 가능한 경로가 없는 경우, -1을 반환합니다.
    if not ans:
        return "-1"

    # 가능한 경로 중 사전 순으로 가장 앞서는 것을 반환합니다.
    return min(ans)

# 메인 함수를 실행합니다.
print(osj())