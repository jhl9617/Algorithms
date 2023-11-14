# https://www.acmicpc.net/problem/1946
# 신입사원 



# --------시작--------
T = int(input())

for _ in range(T):
    # 지원자 수
    N = int(input())
    # 지원자들의 서류, 면접 순위 리스트
    apply = [list(map(int, input().split())) for _ in range(N)]
    # [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
    
    # 서류 순위로 정렬
    apply.sort()
    print(apply)
    # 서류 1등의 면접 순위
    interview = apply[0][1]
    
    cnt = 1
    for i in range(1, N):
        # 면접 순위가 더 높은 지원자가 있으면
        if apply[i][1] < interview:
            # 다음 지원자의 면접 순위로 변경
            interview = apply[i][1]
            print("증가: ",apply[i])
            cnt += 1

    print(cnt)
