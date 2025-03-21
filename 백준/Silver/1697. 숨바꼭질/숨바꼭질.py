import sys
sys.setrecursionlimit(10**6)
n,k = map(int, input().split())

INF = int(1e9)

from collections import deque

visited = [0] * 100001

def bfs(v):
    q = deque([])
    q.append(v)
    while q:
        now = q.popleft()
        if now == k:
            return
        for next in [now-1, now+1, now*2]:
            if next<0 or next>100000:
                continue
            if not visited[next]:
                visited[next] = visited[now]+1
                q.append(next)
bfs(n)
print(visited[k])
