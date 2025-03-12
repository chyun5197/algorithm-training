
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 물건개수n, 최대무게k
n, k = map(int, input().split())
bags = [(0,0)]
for _ in range(n):
    # 무게w, 가치v
    w,v = map(int, input().split())
    bags.append((w,v))

# knapsack(배낭, 냅색) 알고리즘
# 세로n, 가로k | 테이블은 0~(k+1), 0~(n+1) 세팅 : 아래에서 dp[i-1][j] 연산 인덱스 범위때문
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# 테이블 그려야함
for i in range(1, n+1): # 개수n
    for j in range(1, k+1): # 무게j
        weight = bags[i][0] # 현재 무게
        value = bags[i][1] # 현가
        if weight > j: # 현재 무게가 탐색 무게 오버이면
            dp[i][j] = dp[i-1][j] # 이전 개수 최대 가치 할당
        else: # 현재 무게가 탐색 무게 이내이면
            # 이전 개수 최대 가치 vs (현가 + 이전 개수 (탐색무게-현재무게) 시점의 최대 가치)
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])
print(dp[n][k])




# (시간초과)dfs로 접근하면 프로그래머스 <피로도>와 비슷
# maxV = 0 # 최대 가치
# visited = [False] * len(bags)
# def dfs(bags, visited, weight, value):
#     global k, maxV
#     if value>maxV:
#         maxV = value
#     for i in range(len(bags)):
#         if not visited[i] and weight+bags[i][0]<=k:
#             visited[i] = True
#             dfs(bags, visited, weight+bags[i][0], value+bags[i][1])
#             visited[i] = False
# dfs(bags, visited, 0, 0)
# print(maxV)
