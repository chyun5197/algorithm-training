import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

count = 0
house = []
t = 0
def dfs(x,y):
    global t
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if graph[x][y] == 0: # 없는곳 일때는
        return False
    if graph[x][y] == 1: # 방문하지 않은 있는곳이면
        graph[x][y] = 2 # 방문처리를 하고
        t += 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True # 방문처리가 되면 True
    return False

for i in range(n):
    for j in range(n):
        t = 0
        if dfs(i,j) == True:
            count += 1
        if t!=0:
            house.append(t)
print(count)
for i in sorted(house):
    print(i)
# print(*graph, sep='\n')