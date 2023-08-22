# https://www.acmicpc.net/problem/28117
# prlong longf

# 28117번

def func(s, pos):
    if pos >= len(s):
        return 1  # Base case: 끝까지 도달한 경우 하나의 경우의 수 증가

    count = 0
    
    # 현재 위치 기준 "longlong"으로 시작되면
    if s.startswith("longlong", pos):
        count += func(s, pos + 8)  # "longlong" 이후의 문자열을 탐색합니다.

    # 현재 위치 기준 "longlong"으로 시작되지 않으면
    count += func(s, pos + 1)  # 다음 위치의 문자를 탐색합니다.
    
    return count

    
N = int(input())
s = input()
print(func(s, 0))