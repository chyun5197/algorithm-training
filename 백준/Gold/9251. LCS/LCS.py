import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = input().rstrip()
b = input().rstrip()

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]: #
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(max(map(max,dp)))

# (조합) 당연히 시간초과
# if len(a) <= len(b):
#     short, long = a,b
# else:
#     short, long = b,a
# from itertools import combinations
# max = 0
# for i in range(1, len(short)+1):
#     for combs in combinations(short, i):
#         count = 0
#         idx = 0
#         for word in combs:
#             if long.find(word) >= idx:
#                 count+=1
#                 idx = long.find(word)
#             else:
#                 break
#
#         if count>max:
#             max = count
# print(max)
