from collections import deque
from itertools import permutations
def solution(k, dungeons):
    max = 0
    for duns in permutations(dungeons):
        e = k
        ans = 0
        for dun in duns:
            if e>=dun[0]:
                e-=dun[1]
                ans += 1
        if ans>max: 
            max=ans
    return max