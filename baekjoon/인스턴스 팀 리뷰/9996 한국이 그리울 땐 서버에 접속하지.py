# https://www.acmicpc.net/problem/9996
# 한국이 그리울 땐 서버에 접속하지

N = int(input())
pattern = input().split('*')
for _ in range(N): 
    file_name = input()
    if file_name.startswith(pattern[0]) and file_name.endswith(pattern[1]) and len(file_name) >= len(pattern[0]) + len(pattern[1]):
        print('DA')
    else:
        print('NE')