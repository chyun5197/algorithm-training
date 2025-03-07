import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 세로n, 가로m
m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
queue = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
max = 1
def bfs(x,y): # 1번씩만 진행
    global max
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m or graph[nx][ny]==-1:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
            if graph[nx][ny] > max:
                max = graph[nx][ny]
while queue:
    v = queue.popleft()
    bfs(v[0], v[1])

flag = 0
for datas in graph:
    if 0 in datas:
        flag = 1
        break
if flag:
    print(-1)
else:
    print(max-1)







