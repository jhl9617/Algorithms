# https://www.acmicpc.net/problem/29155
# 개발자 지망생 구름이의 취업 뽀개기
 
# 문제 수
N = int(input())

# 난이도별 문제 수(index가 난이도)
numOfProb = list(map(int, input().split()))

# [[], [], [], [], []]
problems = [[] for _ in range(5)]

# 난이도와 소요시간 쌍
for _ in range(N):
    tmp = list(map(int, input().split()))
    
    problems[tmp[0]-1].append(tmp[1])
# [[4, 4, 1, 4, 7], [7, 5], [20], [40], [100]]

# 난이도별 문제를 소요시간 오름차순으로 정렬
for i in range(5):
    problems[i].sort()
# [[1, 4, 4, 4, 7], [5, 7], [20], [40], [100]]

# 문제와 문제 사이의 난이도가 같다면 휴식시간은 두 문제를 푸는데 걸린 시간의 차이
# 문제와 문제 사이의 난이도가 다르다면 휴식시간은 60분
result = 0
for i in range(5):
    for j in range(1, numOfProb[i]+1):
        
        if j == 1:
            # 난이도의 첫번째 문제는 휴식시간이 없음
            result += problems[i][j-1]
        else:
            # 난이도의 두번째 문제부터는 해당 문제 푸는시간*2 - 이전 문제 푸는시간 
            result += problems[i][j-1]*2  - problems[i][j-2]
        
    if i != 4:
        result += 60

print(result)

