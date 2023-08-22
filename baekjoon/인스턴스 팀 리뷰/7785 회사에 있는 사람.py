# https://www.acmicpc.net/problem/7785

# set을 이용
# 순서가 필요없고, 중복을 허용하지 않음

n = int(input())
log = set()
for _ in range(n):
    name, action = input().split()
    if action == 'enter':
        log.add(name)
    else:
        log.remove(name)

for name in sorted(log, reverse=True):
    print(name)
