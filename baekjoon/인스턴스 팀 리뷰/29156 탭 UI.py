# https://www.acmicpc.net/problem/29156
# 탭 UI

import sys

def find_position(tabs, L, clicks):
    
    # 탭들의 합 20
    sum_tabs = sum(tabs)

    # 화면의 절반 5
    half_screen = L / 2

    results = []

    for tab in clicks:
        # 선택한 탭 앞의 모든 탭 더하고 선택한 탭의 절반을 더함
        tab_center = sum(tabs[:tab-1]) + tabs[tab-1] / 2

        # 화면의 왼쪽 끝
        position = tab_center - half_screen
        # print(position) 시 -4, -2, 0, 2, 4, 6, 8, 10, 12, 14

        # 화면의 길이가 탭들의 합보다 크면
        if sum_tabs <= L:
            position = 0
        # 화면의 왼쪽 끝에 위치하거나 화면의 오른쪽 끝에 위치하면
        elif position < 0: 
                position = 0
        elif position + L > sum_tabs: 
                position = sum_tabs - L

        results.append(position)

    return results

# 탭의 갯수
N = int(sys.stdin.readline().rstrip())

# 각 탭의 길이
tabs = []
for _ in range(N):
    tabs.append(int(sys.stdin.readline().rstrip()))

# 화면의 길이
L = int(sys.stdin.readline().rstrip())
# 클릭한 탭의 갯수
Q = int(sys.stdin.readline().rstrip())

clicks = []
current = 0
# 클릭한 탭의 번호
for _ in range(Q):
    clicks.append(int(sys.stdin.readline().rstrip()))

positions = find_position(tabs, L, clicks)
for pos in positions:
    sys.stdout.write("{:.2f}\n".format(pos))