# 참고함) https://chaeyami.tistory.com/184
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부이면서 부모 노드를 저장한다.
visited = [False] * (n+1)

def dfs(graph, v, visited): # v는 노드
    for i in graph[v]: # 해당 노드에 인접한 노드 중에서
        if not visited[i]: # 방문한 적이 없다면
            visited[i] = v # 해당 노드를 부모 노드로 저장
            dfs(graph, i, visited)

dfs(graph, 1, visited)

for v in range(2, n+1):
    print(visited[v])