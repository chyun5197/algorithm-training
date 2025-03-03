# 이진 트리 아니였음
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split()) # 부모, 자식, 가중치
    graph[a].append((b,c))
    graph[b].append((a,c))



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

'''
5
1 2 3
1 3 3
2 4 5
2 5 7
=>13

4
1 2 1
1 3 5
1 4 2
=> 7

5
1 2 100
1 3 100
2 4 100
3 5 1
=> 301
'''


