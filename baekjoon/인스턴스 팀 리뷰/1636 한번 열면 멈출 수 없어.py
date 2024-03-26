# https://www.acmicpc.net/problem/1636
# 한번 열면 멈출 수 없어
def eat(N, pringles, current=0, last_stress=0, total_loss=0, path=[], result=[210000000, []]):
    # 다먹음
    if current == N:
        if total_loss < result[0]:
            result[0] = total_loss
            result[1] = path[:]
        return
    
    # 재귀
    for stress in range(pringles[current][0], pringles[current][1] + 1):
        if current == 0:  
            eat(N, pringles, current + 1, stress, 0, [stress], result)
        else:
            loss = abs(last_stress - stress)
            eat(N, pringles, current + 1, stress, total_loss + loss, path + [stress], result)

    return result

# ---------시작----------
N = int(input())
pringles = []
for i in range(N):
    a,b = map(int,input().split())
    pringles.append((a,b))
lost, stresses = eat(N, pringles)

print(lost)
for stress in stresses:
    print(stress)
