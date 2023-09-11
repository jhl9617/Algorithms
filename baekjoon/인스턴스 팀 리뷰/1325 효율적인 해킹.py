# https://www.acmicpc.net/problem/1325

import sys

def input():
    return sys.stdin.readline().rstrip()

# 인접이스트로 그래프를 만듦
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
# graph = [[], [3], [3], [4, 5], [], []]

# (i, count) 형태로 저장
result = []
for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True
    stack = [i]
    count = 1
    # DFS
    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            # 방문 안한 노드가 발견되면 방문처리하고 스택에 추가
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
                count += 1
    result.append((i, count))

# 2번째 행의 값을 기준으로 내림차순 정렬
# -x[1] : x의 2번째 요소(-는 내림차순), x[0] : 타이 브레이커 
result.sort(key=lambda x: (-x[1], x[0]))
max_value = result[0][1]
for i in range(N):
    if result[i][1] == max_value:
        print(result[i][0], end=' ')
    else:
        break