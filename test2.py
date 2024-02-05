from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
group = [0] * (N+1)  # 원숭이들을 나눌 그룹(1 또는 -1), 0은 아직 그룹이 정해지지 않음을 의미

# 그래프 구성
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for enemy in data[1:]:
        adj[i].append(enemy)
        adj[enemy].append(i)  # 무방향 그래프

def bfs(start):
    q = deque([start])
    group[start] = 1  # 시작 정점을 그룹 1에 할당
    while q:
        cur = q.popleft()
        for neighbor in adj[cur]:
            if group[neighbor] == 0:  # 아직 방문하지 않은 정점
                group[neighbor] = -group[cur]  # 이웃한 정점은 다른 그룹에 할당
                q.append(neighbor)
            elif group[neighbor] == group[cur]:  # 이미 방문한 정점이면서 같은 그룹이라면 이분 그래프가 아님
                return False
    return True

# 모든 정점에 대해 BFS 수행
is_bipartite = True
for i in range(1, N+1):
    if group[i] == 0:  # 아직 방문하지 않은 정점에 대해서만 BFS 수행
        if not bfs(i):
            is_bipartite = False
            break

if is_bipartite:
    first_prison = [i for i in range(1, N+1) if group[i] == 1]
    second_prison = [i for i in range(1, N+1) if group[i] == -1]
    print(len(first_prison), *first_prison)
    print(len(second_prison), *second_prison)
else:
    print("조건에 맞게 원숭이들을 나눌 수 없습니다.")
