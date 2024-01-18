# 입력값을 받습니다. (명령의 길이 N, 오세준의 위치 SejunX, SejunY, 지뢰의 위치 mineX, mineY)
n, x, y, x1, y1 = map(int, input().split())

# 오세준이 지뢰의 위치에 도달할 수 없는 경우를 체크합니다.
if x1 < x or y1 < y:
    print(-1)  # 지뢰가 오세준보다 왼쪽이나 아래에 있으면 도달 불가능합니다.
elif x == x1:
    # 오세준이 지뢰와 같은 x축에 있을 때, 오직 위로만 이동해야 합니다.
    if n >= (y1 - y):
        print('U' * (y1 - y) + 'R' * (n - y1 + y))
    else:
        print('U' * n)
elif y == y1:
    # 오세준이 지뢰와 같은 y축에 있을 때, 오직 오른쪽으로만 이동해야 합니다.
    print('R' * n)
else:
    # 가능한 경로를 저장할 리스트를 초기화합니다.
    r = []

    # 'R'과 'U' 명령의 조합을 탐색합니다.
    for i in range(1, n):
        a = n - i  # 오른쪽으로 이동할 횟수
        b = i      # 위로 이동할 횟수

        dif_x = x1 - x  # 오세준과 지뢰 사이의 x축 거리
        dif_y = y1 - y  # 오세준과 지뢰 사이의 y축 거리

        moc_a = dif_x // a  # x축 거리를 오른쪽 이동 횟수로 나눈 몫
        moc_b = dif_y // b  # y축 거리를 위로 이동 횟수로 나눈 몫

        # 'R'과 'U'의 비율이 거의 같거나 1 차이 날 때 가능한 경로를 찾습니다.
        if abs(moc_a - moc_b) <= 1:
            r_a = dif_x - (moc_a * a)  # 'R' 명령의 실제 이동 횟수
            r_b = dif_y - (moc_b * b)  # 'U' 명령의 실제 이동 횟수
            result = 'R' * r_a + 'U' * r_b + 'R' * (a - r_a) + 'U' * (b - r_b)
            r.append(result)  # 가능한 경로를 리스트에 추가합니다.

    # 가능한 명령 시퀀스 중 사전순으로 가장 앞서는 것을 선택합니다.
    if not r:
        print(-1)  # 가능한 경로가 없으면 -1을 출력합니다.
    else:
        r.sort()  # 가능한 경로들을 사전 순으로 정렬합니다.
        print(r[0])  # 가장 앞서는 경로를 출력합니다.
