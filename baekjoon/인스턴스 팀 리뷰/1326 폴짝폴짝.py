from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
a, b = map(int, input().split())
visited = [-1] * n

def bfs(start, finish, n, graph):

    q = deque([start - 1])
    # 시작 징검다리는 0번 점프로 방문
    visited[start - 1] = 0

    while q:
        # 현재 징검다리를 큐에서 꺼냄
        node = q.popleft()
        
        # 현재 징검다리에서 앞쪽으로 점프 가능한 징검다리들을 탐색
        for i in range(node, n, graph[node]):
            print(i, end=' ')
            if visited[i] == -1:
                # 큐에 넣고 방문 처리한다.
                q.append(i)
                visited[i] = visited[node] + 1

                if i == finish - 1:
                    return visited[i]
        
        # 현재 징검다리에서 뒤쪽으로 점프 가능한 징검다리들을 탐색
        for i in range(node, -1, -graph[node]):
            # //range 출력
            print(i, end=' ')
            if visited[i] == -1:
                # 큐에 넣고 방문 처리한다.
                q.append(i)
                visited[i] = visited[node] + 1

                if i == finish - 1:
                    return visited[i]
    
    return -1

answer = bfs(a, b, n, graph)
print(answer)
