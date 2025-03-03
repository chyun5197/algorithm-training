import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    datas = list(map(int, input().split()))[:-1]
    a = datas[0] # 맨앞은 시작노드
    b = datas[1::2] # 타겟노드
    c = datas[2::2] # 거리
    m = len(b) # 간선 개수
    for i in range(m):
        graph[a].append((b[i],c[i]))

# print(*graph, sep='\n')

def dfs(graph, v, dis):
    for n, d in graph[v]:
        if dis[n] == 0:
            dis[n] = dis[v] + d
            dfs(graph, n, dis)

# 루트부터 최장거리인 노드 탐색
dis = [0] * (n+1)
dfs(graph,1, dis)
maxNode = dis.index(max(dis))
# print(maxNode)

# 최장거리노드로부터 최대거리 탐색
dis = [0] * (n+1)
dfs(graph, maxNode, dis)
dis[maxNode] = 0
print(max(dis))