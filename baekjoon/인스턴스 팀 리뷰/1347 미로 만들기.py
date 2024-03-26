# https://www.acmicpc.net/problem/1347
# 미로 만들기

# 가정 1 : 리스트를 최대 크기로 미리 만들어 놓고 시작한다.
# 가정 2 : 리스트를 1 * 1 에서 시작하여 현재 크기를 벗어날때 마다 리스트의 크기를 1씩 늘린다.

# 기본으로 모든 리스트를 #로 채우고 시작한다. 

import sys

N = int(sys.stdin.readline().rstrip())
commands = sys.stdin.readline().rstrip()

# direction + 는 오른쪽으로 돌기. - 는 왼쪽으로 돌기.
Dy = (-1,0,1,0)
Dx = (0,1,0,-1)
maze = [['#' for _ in range(101)] for _ in range(101)]
y, x, direction = 50, 50, 2
ey = ex = sy = sx = 50
maze[y][x] = '.'

for command in commands:
    if command == 'L': direction = (direction - 1) % 4
    elif command == 'R': direction = (direction + 1) % 4

    # 앞으로 감
    else:
        y, x = y + Dy[direction], x + Dx[direction]
        maze[y][x] = '.'
        sy, ey, sx, ex = min(sy, y), max(ey, y), min(sx, x), max(ex, x)

for i in range(sy, ey+1): 
    for j in range(sx, ex+1): 
        print(maze[i][j], end='')
    print()