# https://www.acmicpc.net/problem/14501
# 퇴사

# --------시작--------
N = int(input())
# 상담 기간, 금액 리스트
consult = [list(map(int, input().split())) for _ in range(N)]

max_profit = 0

# dp[i] = i일까지의 최대 수익
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    # i일에 상담을 할 수 있으면
    if i + consult[i][0] <= N:
        #  i일에 상담을 선택하였을 때와 선택하지 않았을 때
        # dp[i + consult[i][0]] :  i일에 상담을 선택한 후, 
        # 상담이 끝난 다음에 시작할 수 있는 상담으로부터 얻을 수 있는 최대 수익
        dp[i] = max(consult[i][1] + dp[i + consult[i][0]], max_profit)
        max_profit = dp[i]
    # i일에 상담을 할 수 없으면
    else:
        
        dp[i] = max_profit
        # print("상담 불가: ", consult[i])
    
    
print(max_profit)

# 예제 1번일 경우 dp 출력
# [0, 0, 0, 0, 0, 0, 0, 0] i = 0 상담 불가
# [0, 0, 0, 0, 0, 0, 0, 0] i = 1 상담 불가
# [0, 0, 0, 0, 15, 0, 0, 0] i = 2
# [0, 0, 0, 35, 15, 0, 0, 0] i = 3
# [0, 0, 45, 35, 15, 0, 0, 0] i = 4
# [0, 45, 45, 35, 15, 0, 0, 0] i = 5
# [45, 45, 45, 35, 15, 0, 0, 0] i = 6
