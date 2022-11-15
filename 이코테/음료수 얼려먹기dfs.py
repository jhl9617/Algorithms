
# dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문

def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if nums[x][y] == 0:

        #해당 노드 방문 처리
        nums[x][y] = 1
        #상 하 좌 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = 4, 5
nums = []
for i in range(n):
    nums.append(list(map(int, input())))
print(nums)

result = 0
for i in range(n):
    for j in range(m):
        
        if dfs(int(i),int(j)) == True:
            result += 1
print(result)
print(nums)