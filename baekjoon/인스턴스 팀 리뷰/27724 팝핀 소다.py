# https://www.acmicpc.net/problem/27724
# 팝핀 소다

import math

# # 8 2 4
# # N 선수의 수 8
# # M 이변의 수 2
# # K 탄산 내성 4
# ----------시작----------
n, m, k = map(int, input().split())

total_game = int(math.log(n, 2))
print(total_game)
win = int(math.log(k, 2))

# 시은이가 이길수 있는 최대 게임 수를 구하는 것이므로 이변 값을 더해줌
# 하지면 최대 게임 수를 넘을수는 없음
print(min(win + m, total_game))