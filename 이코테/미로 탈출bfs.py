from collections import deque

def bfs(x, y):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    #큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()

        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #미로 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny >= m:
                continue

            #벽인경우 무시
            if graph[nx][ny] == 0:
                continue

            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                #               바로 직전 노드에서의 최단거리 + 1을 삽입
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


#n, m을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
#2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#bfs를 수행한 결과 출력
print(bfs(0, 0))

"""
input 
5 6
101010
111111
000001
111111
111111
"""