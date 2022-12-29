from itertools import product

N, M = map(int, input().split())

ans = []

def back():
    if len(ans) == M:   #배열의 길이를 확인
        print(" ".join(map(str, ans)))  #1 2 3 이런 상태로 출력
        return
    for i in range(1, N + 1):
        if i not in ans:
            ans.append(i)
