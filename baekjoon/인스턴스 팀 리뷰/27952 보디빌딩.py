# https://www.acmicpc.net/problem/27952
# 보디빌딩
# X = 루틴을 진행할 때마다 무게가 X만큼 감소(하루에 여러번 가능 )
# N = 루틴을 진행할 날의 수
# i번째 날에 몸무게가 최소 A[i]는 되어야 한다(이하면 쓰러짐)
# i번째 날에 B[i]만큼 찐다

# -------------시작--------------
N, X = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_routines = 0  
current_weight = 0

for i in range(N):
    current_weight += B[i]

    # 현재 몸무게가 A[i]보다 적으면
    if current_weight <= A[i]:
        print(-1)
        exit()

    # 가능 루틴 계산
    today = (current_weight - A[i]) // X

    # 루틴 수행
    total_routines += today
    current_weight -= today * X

print(total_routines)
# -------------끝--------------
