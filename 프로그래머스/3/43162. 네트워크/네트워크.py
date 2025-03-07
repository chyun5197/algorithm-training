# dfs
def solution(n, computers):
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i==j: 
                continue
            elif computers[i][j] == 1:
                graph[i+1].append(j+1)
            # a,b = i, computers[i][j]
    
    visited = [False] * (n+1)
    
    # []
    # [2]
    # [1]
    # []
    print(*graph, sep='\n')
    
    from collections import deque
    # bfs로 같은 네트워크는 방문처리 True
    def bfs(graph, v, visited): # 방문한적 없으면 새로 방문처리
        if visited[v]: # 방문한적 있으면 카운트X
            return False
        # 방문없으면 네트워킹하고 방문처리 True 리턴 카운트
        queue = deque([])
        queue.append(v)
        visited[v] = True
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
        return True 
                
    answer = 0
    for data in range(1, n+1):
        if bfs(graph, data, visited):
            answer += 1
    
    return answer