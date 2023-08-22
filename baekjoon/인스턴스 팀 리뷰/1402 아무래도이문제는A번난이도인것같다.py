# https://www.acmicpc.net/problem/1402


# A가 1*1*1*1.... 혹은 -1*-1*-1*-1... 이 될수 있으므로 무조건 yes
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print('yes')

