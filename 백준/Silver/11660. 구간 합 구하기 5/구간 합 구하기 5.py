import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
a = [list(map(int,input().split())) for _ in range(n)]
test = []
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    test.append((x1,y1,x2,y2))

# print(*a, sep='\n')

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
# for i in range(n):
#     for j in range(n):
#         if i==0 and j==0:
#             dp[i][j] = a[i][j]
#         elif j==0:
#             dp[i][j] = a[i][j] + dp[i-1][-1]
#         else:
#             dp[i][j] = a[i][j] + dp[i][j-1]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = a[i-1][j-1] + dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]


# print(*dp, sep='\n')

for x1,y1,x2,y2 in test:
    sum = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(sum)


