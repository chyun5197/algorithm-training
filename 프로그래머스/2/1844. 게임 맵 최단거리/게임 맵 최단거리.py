from collections import deque

def solution(maps):
    n,m = len(maps),len(maps[0]) # 세로n, 가로m
    graph = [[0 for i in range(m)] for j in range(n)] # 각 위치마다 최소 거리 저장

    dx = [-1,1,0,0] 
    dy = [0,0,-1,1]
    
    q = deque([])
    q.append((0, 0))
    graph[0][0] += 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m or maps[nx][ny] == 0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

    # print(graph[n-1][m-1])
    answer = graph[n-1][m-1] if graph[n-1][m-1]>0 else -1
        
    return answer