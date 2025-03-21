n,k = map(int, input().split())
from collections import deque
visited = [0] * 100001

def bfs(v):
    q = deque([])
    q.append(v)
    while q:
        now = q.popleft()
        if now == k:
            return
        for next in [now*2,now-1, now+1]:
            if next<0 or next>100000 or visited[next]:
                continue
            if now*2 == next:
                visited[next] = visited[now]
                q.append(next)
            else:
                visited[next] = visited[now] + 1
                q.append(next)

bfs(n)
print(visited[k])