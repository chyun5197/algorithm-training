import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) 
n = int(input())
graph = [list(map(str, input().rstrip())) for i in range(n)]
# print(graph)
c1 = 0 # 일반

import copy # 시간초과날듯
graph2 = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'G':
            graph2[i][j] = 'R'
c2 = 0 # 적록색약

def dfs(x,y,g):
    global now
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if g[x][y] == 1: # 지났으면
        return False
    if g[x][y] == now: # 같은 값이면
        g[x][y] = 1
        # c1 += 1
        dfs(x+1,y, g)
        dfs(x-1,y, g)
        dfs(x,y-1, g)
        dfs(x,y+1, g)
        return True # 방문처리가 되면 True
    return False

for i in range(n):
    for j in range(n):
        now = graph[i][j]
        if dfs(i, j, graph) == True:
            c1 += 1

        now = graph2[i][j]
        if dfs(i, j, graph2) == True:
            c2 += 1
print(c1)
print(c2)
# print(*graph, sep='\n')
# print()
# print(*graph2, sep='\n')

